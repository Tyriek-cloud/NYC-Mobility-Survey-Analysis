# NYC-Mobility-Survey-Analysis
This was an end-to-end data engineering project that was designed to derive insights from the New York City Department of Transportation's 2022 Citywide Mobility Survey. Five NYC DOT datasets were extracted to an s3 bucket, transformed and loaded into a database, and loaded into AWS Quicksight for analysis.

# Step 1: Identity Access Management (IAM)
Despite the fact that I am the only person on this project, I decided to exercise good Identity Access Management practices. I created a user (myself) and attached the permission policies directly. For the most part, the user has full access to all the assigned services (no Policy Boundary). The list of permissions that I assigned to the user are listed below:

![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/b1773fe0-bd1c-4c77-9e32-9ad54e49773b)

# Step 2: Creating s3 Bucket
We begin by creating a s3 Bucket. A standard s3 Bucket will be fine for this use case. It is important to pick an easily recognizable name for this project, but everything else should be the default.

![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/69178f6f-2d84-4ccf-a860-1feef1a50825)

The staging folder will contain all of five of the datasets that were extracted into AWS. The warehouse folder will contain the transformed data. The data will be changed into parquet format for easier management (quite helpful because one of the datasets is quite large).

![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/e34b5fbc-d465-4449-903e-8e535bb9c25d)

Here is a peak at the datasets in the staging folder. They are all in CSV format (it is possible to extract them into another preferred file format from NYC Open Data).

![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/c9e781e6-4b04-4a22-8ad1-453205117c0b)

# Step 3: A Complex Inner Join Schema in AWS Glue
![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/a4e9e992-72d6-4f91-9a06-c882830837a9)

Everything is either joined on the hh_id or the person_id

# Step 4: Run the Glue Job
![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/38023dde-5f8e-418b-9063-bb3461ac99c0)

![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/8a2c23c3-ca11-4335-80cd-175278f2223b)

# Step 5: Create a Database to be Crawled
![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/a0947851-ec4f-488b-9167-4fec43030b49)

# Step 6: Analyze and Visualize the Data with Quicksight
![image](https://github.com/Tyriek-cloud/NYC-Mobility-Survey-Analysis/assets/62261407/e749bb4c-43cf-4572-bc38-f8bc47df6445)

Sources:
https://data.cityofnewyork.us/Transportation/Citywide-Mobility-Survey-Vehicle-2022/qyry-gwrj

https://data.cityofnewyork.us/Transportation/Citywide-Mobility-Survey-Day-2022/5njs-bq3c

https://data.cityofnewyork.us/Transportation/Citywide-Mobility-Survey-Trip-2022/x5mc-2gmi

https://data.cityofnewyork.us/Transportation/Citywide-Mobility-Survey-Household-2022/dt3g-khpi

https://data.cityofnewyork.us/Transportation/Citywide-Mobility-Survey-Person-2022/7qdz-u9hr

