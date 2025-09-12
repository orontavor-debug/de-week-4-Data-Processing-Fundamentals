# Solution: Designing a Production-Grade Enriched Data Pipeline and Loading into Metabase


## Step-by-Step Solutions

### Step 1: Ensure Docker is Running
Follow steps listed here: [Docker Setup](https://github.com/LD-LINC/Week-4---Data-Processing-Fundamentals/blob/main/03_Data_pipeline_design_%26_data_quality/Solution/Activity_1_Creating%20a%20data%20pipeline%20with%20quality%20checks.md)

---

### Step 2 and 3 : Enrich Data with External Sources

For all the step 2 and 3 code, check below code with explanation.

[Enrichment_Code](https://github.com/LD-LINC/Week-4---Data-Processing-Fundamentals/blob/eae8ba3ab6f076457d021fcafd25860c1608424e/04_weekly_project/04_weekly_project.ipynb)



### Step 4: Set Up Metabase

1. Download and run Metabase as a Docker container.  Execute command `docker run -d -p 3000:3000 metabase/metabase`
2. Access Metabase from `http://localhost:3000/` . Provided your postgres details to connect to db from metabase.
   
<p align="center">
   
![ETL Pipeline](assets/metabase_connection.png)

</p>

3. Connect Metabase to your Postgres database.


<p align="center">
   
![ETL Pipeline](assets/metabase_database.png)

</p>



