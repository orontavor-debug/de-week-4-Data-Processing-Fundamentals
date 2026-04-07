import pandas as pd
from sqlalchemy import create_engine
import os
import requests
import json
from bs4 import BeautifulSoup
import numpy as np

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{db_user}:{db_password}@db:5432/{db_name}") #start postgress

df = pd.read_csv('Northwind.csv') #read original northwind table
try:
    df.to_sql('fct_tblnorthwind', engine, if_exists='fail', index=False)
    print("fct_tblnorthwind created and loaded successfully!")
except ValueError:
    print("fct_tblnorthwind already exists, skipping")

dates = pd.read_sql("SELECT DISTINCT \"orderDate\" FROM fct_tblnorthwind", engine)['orderDate'].tolist() #get a list of dates from the fct table
start_date = min(dates) #store min/max dates to use later for the api call
end_date = max(dates)

url = "https://archive-api.open-meteo.com/v1/archive" # store the api call in a var
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "start_date": str(start_date),
    "end_date": str(end_date),
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "timezone": "Europe/Berlin"
}

response = requests.get(url, params=params) # fetch berlin weather from api
data = response.json()      #parse response to json
# print(json.dumps(data, indent=2)) # see how data is layed out from the api, in json

weather_df = pd.DataFrame({ #store api call in a dataframe
    'date': data['daily']['time'],
    'temp_max': data['daily']['temperature_2m_max'],
    'temp_min': data['daily']['temperature_2m_min']
})
weather_df['avg_daily_temp'] = (weather_df['temp_max'] + weather_df['temp_min']) / 2

weather_df.to_sql('weather_data', engine, if_exists='replace', index=False) #save to db, replace all data in each run
print("weather_data loaded")

quotes = [] #scrape first 5 pages
for i in range(1, 6):
    url = f"http://quotes.toscrape.com/page/{i}/"
    response = requests.get(url) #download html
    soup = BeautifulSoup(response.text, 'html.parser')
    quote_divs = soup.find_all("div", class_="quote") #find quotes top level
    for quote_div in quote_divs:
        quote_text = quote_div.find("span", class_="text").text #extract actual quote
        quotes.append(quote_text)

df_quotes = pd.DataFrame({ #store quotes in a dataframe
    "quotes": quotes
})

try:
    df_quotes.to_sql('quotes_table',engine , if_exists='replace', index=False) #save to db, replace all data in each run
    print("quotes_table created")
except ValueError:
    print("quotes_table already exists")

#read tables to dataframes
df_fct = pd.read_sql("SELECT * FROM fct_tblnorthwind", engine)
# drop columns that will be re-added by the merge to avoid duplicates
df_fct = df_fct.drop(columns=['avg_temp_order_date', 'random_quote', 'date'], errors='ignore')
df_weather = pd.read_sql("SELECT * FROM weather_data", engine)
df_quotes = pd.read_sql("SELECT * FROM quotes_table", engine)

df_enriched = df_fct.merge(df_weather[['date', 'avg_daily_temp']], left_on='orderDate', right_on='date', how='left') #merge the dataframes into one table, join on date
df_enriched = df_enriched.drop(columns=['date'], errors='ignore')
df_enriched = df_enriched.rename(columns={'avg_daily_temp': 'avg_temp_order_date'}) #rename column
df_enriched['random_quote'] = np.random.choice(df_quotes['quotes'], size=len(df_enriched)) #grab a random quote
df_enriched.to_sql('fct_tblnorthwind', engine, if_exists='replace', index=False) # write to db

 
 #reporting tables from enriched table
rpting_customers = df_enriched[['customerID', 'companyName', 'contactName', 'contactTitle', 'random_quote']]
rpting_customers.to_sql('rpt_customers', engine, if_exists='replace', index=False)

rpting_orders = df_enriched[['orderID', 'customerID', 'orderDate', 'requiredDate', 'shippedDate', 'quantity', 'avg_temp_order_date']]
rpting_orders.to_sql('rpt_orders', engine, if_exists='replace', index=False) 