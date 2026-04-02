import pandas as pd
from sqlalchemy import create_engine,text
import os
from datetime import datetime

df = pd.read_csv('Northwind_errors.csv', encoding='latin-1')

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{db_user}:{db_password}@db:5432/{db_name}")

df.to_sql('tblnorthwind', engine, if_exists='replace', index=False)

df.columns = (df.columns
              .str.lower() # lowercolumns
              .str.replace('.', '', regex=False)  # remove dots
              .str.replace(' ', '_', regex=False)) # replace spaces

for col in ['orderdate', 'requireddate', 'shippeddate']: ## cast date
    df[col] = pd.to_datetime(df[col]).dt.date

df.to_sql('land_tblnorthwind', engine, if_exists='replace', index=False) #load fixed data

with engine.connect() as conn: #compare num of rows
    count_raw = conn.execute(text("SELECT COUNT(*) FROM tblnorthwind")).scalar()
    count_land = conn.execute(text("SELECT COUNT(*) FROM land_tblnorthwind")).scalar()
    
    if count_raw != count_land:
        print("Error: row counts don't match between both tables!")
        exit()

df.to_sql('tblnorthwind_error', engine, if_exists='replace', index=False) # create error table

with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS tblnorthwind_error"))
    conn.execute(text("CREATE TABLE tblnorthwind_error AS SELECT *, NULL::text AS error_reason FROM land_tblnorthwind WHERE 1=0"))
    conn.commit()

#data integrity checks
null_check = df[df['orderid'].isna() | df['customerid'].isna()].copy() # check null orderid or customerid
null_check['error_reason'] = 'orderid or customerid is null'
null_check.to_sql('tblnorthwind_error', engine, if_exists='append', index=False) #load error to table
date_check = df[df['orderdate'] < datetime(1990, 1, 1).date()].copy() # check if date before 1990
date_check['error_reason'] = 'date is prior to 1990'
date_check.to_sql('tblnorthwind_error', engine, if_exists='append', index=False)
quantity_check = df[df['quantity'] < 0].copy() # check if quantity is negative
quantity_check['error_reason'] = 'quantity is negative'
quantity_check.to_sql('tblnorthwind_error', engine, if_exists='append', index=False)
char_check=df[df['supplierscontacttitle'].str.match('^\d+$')].copy() #check if there are no digits
char_check['error_reason'] = 'supplierscontacttitle contains only digits'
char_check.to_sql('tblnorthwind_error', engine, if_exists='append', index=False)

df_errors = pd.read_sql("SELECT * FROM tblnorthwind_error", engine)
error_ids = df_errors['orderid'].dropna()  # get error orderids, exclude nulls
correct_records = df[~df['orderid'].isin(error_ids) & df['orderid'].notna()].copy() #store correct records
correct_records['load_date'] = datetime.now().date()
correct_records.to_sql('fct_tblnorthwind', engine, if_exists='replace', index=False) # copy to new facts table

with engine.connect() as conn:
    conn.execute(text("ALTER TABLE fct_tblnorthwind ADD PRIMARY KEY (orderid, productid)"))
    conn.commit()
    
print("Data loaded successfully!")