# Creating a Data Pipeline with Quality Checks

## Objective

This exercise builds on the Docker exercise from **Week 3**.  
This time, the business has provided an **incorrect Northwind file** containing **erroneous records**.  

The objective is to create an **end-to-end data pipeline** that:
- Loads data using the Docker container created in Week 3 (but with the updated file).  
- Performs **quality checks** on the loaded data.  

---

## Instructions

1. Use the `northwind_project_docker` container from Week 3 and place the provided file (with inaccuracies) in the Docker directory.  
   Load this file into the table `tblnorthwind`.

2. Connect to this database using **pgAdmin 4**.  
   Ensure the container is running throughout this exercise.

3. Observe inconsistencies in column names. Based on your observations, create a landing table `land_tblnorthwind` with the following considerations:
   - Convert all column names to **lowercase**.  
   - Cast all date columns (`orderDate`, `requiredDate`, `shippedDate`) to **DATE**.  
   - Remove `.` from column names (e.g., `employees.lastName` → `employeeslastname`).  

4. Load all data from `tblnorthwind` into the landing table `land_tblnorthwind`.

5. Validate record counts:  
   - If counts between `tblnorthwind` and `land_tblnorthwind` do not match, raise an **error** and **exit** the pipeline.

6. Create a table `tblnorthwind_error` to store all **error records**.  
   - Add an additional column `error_reason`.

7. Perform the following **quality checks** on the landing table and move error records into `tblnorthwind_error`:
   - `orderid` and `customerid` must not be NULL.  
   - `orderdate` values earlier than **1990** must be flagged.  
   - `quantity` must not be negative.  
   - Records where `supplierscontacttitle` contains **only digits** must be flagged.  

8. Create a fact table `fct_tblnorthwind` to store only **correct records** . Add additional column load_date for audit purpose.

9. Load all correct records from the landing table into the fact table.

10. Add a **primary key constraint** on the final fact table `fct_tblnorthwind`, considering `(orderid, productid)` as the primary key.


