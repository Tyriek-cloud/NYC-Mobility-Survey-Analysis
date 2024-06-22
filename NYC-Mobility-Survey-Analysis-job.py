import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Day
Day_node1719078284552 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://nyc-mobility-survey-analysis/staging/Citywide_Mobility_Survey_-_Day_2022_20240622.csv"], "recurse": True}, transformation_ctx="Day_node1719078284552")

# Script generated for node Vehicle
Vehicle_node1719078290090 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://nyc-mobility-survey-analysis/staging/Citywide_Mobility_Survey_-_Vehicle_2022_20240622.csv"], "recurse": True}, transformation_ctx="Vehicle_node1719078290090")

# Script generated for node Person
Person_node1719078286883 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://nyc-mobility-survey-analysis/staging/Citywide_Mobility_Survey_-_Person_2022_20240622.csv"], "recurse": True}, transformation_ctx="Person_node1719078286883")

# Script generated for node Trip
Trip_node1719078288622 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://nyc-mobility-survey-analysis/staging/Citywide_Mobility_Survey_-_Trip_2022_20240622.csv"], "recurse": True}, transformation_ctx="Trip_node1719078288622")

# Script generated for node Household
Household_node1719078285940 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://nyc-mobility-survey-analysis/staging/Citywide_Mobility_Survey_-_Household_2022_20240622.csv"], "recurse": True}, transformation_ctx="Household_node1719078285940")

# Script generated for node Join_Vehicle_Person
Join_Vehicle_Person_node1719078697666 = Join.apply(frame1=Vehicle_node1719078290090, frame2=Person_node1719078286883, keys1=["hh_id"], keys2=["hh_id"], transformation_ctx="Join_Vehicle_Person_node1719078697666")

# Script generated for node Join_Person_Day
Join_Person_Day_node1719078514550 = Join.apply(frame1=Day_node1719078284552, frame2=Person_node1719078286883, keys1=["person_id"], keys2=["person_id"], transformation_ctx="Join_Person_Day_node1719078514550")

# Script generated for node Join_Trip_Vehicle
Join_Trip_Vehicle_node1719078854554 = Join.apply(frame1=Trip_node1719078288622, frame2=Vehicle_node1719078290090, keys1=["hh_id"], keys2=["hh_id"], transformation_ctx="Join_Trip_Vehicle_node1719078854554")

# Script generated for node Join_Household_Person
Join_Household_Person_node1719078578757 = Join.apply(frame1=Household_node1719078285940, frame2=Person_node1719078286883, keys1=["hh_id"], keys2=["hh_id"], transformation_ctx="Join_Household_Person_node1719078578757")

job.commit()