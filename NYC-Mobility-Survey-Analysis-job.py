import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

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
Vehicle_node1719078290090DF = Vehicle_node1719078290090.toDF()
Person_node1719078286883DF = Person_node1719078286883.toDF()
Join_Vehicle_Person_node1719078697666 = DynamicFrame.fromDF(Vehicle_node1719078290090DF.join(Person_node1719078286883DF, (Vehicle_node1719078290090DF['hh_id'] == Person_node1719078286883DF['hh_id']), "outer"), glueContext, "Join_Vehicle_Person_node1719078697666")

# Script generated for node Join_Person_Day
Day_node1719078284552DF = Day_node1719078284552.toDF()
Person_node1719078286883DF = Person_node1719078286883.toDF()
Join_Person_Day_node1719078514550 = DynamicFrame.fromDF(Day_node1719078284552DF.join(Person_node1719078286883DF, (Day_node1719078284552DF['person_id'] == Person_node1719078286883DF['person_id']), "outer"), glueContext, "Join_Person_Day_node1719078514550")

# Script generated for node Join_Trip_Vehicle
Trip_node1719078288622DF = Trip_node1719078288622.toDF()
Vehicle_node1719078290090DF = Vehicle_node1719078290090.toDF()
Join_Trip_Vehicle_node1719078854554 = DynamicFrame.fromDF(Trip_node1719078288622DF.join(Vehicle_node1719078290090DF, (Trip_node1719078288622DF['hh_id'] == Vehicle_node1719078290090DF['hh_id']), "outer"), glueContext, "Join_Trip_Vehicle_node1719078854554")

# Script generated for node Join_Household_Person
Household_node1719078285940DF = Household_node1719078285940.toDF()
Person_node1719078286883DF = Person_node1719078286883.toDF()
Join_Household_Person_node1719078578757 = DynamicFrame.fromDF(Household_node1719078285940DF.join(Person_node1719078286883DF, (Household_node1719078285940DF['hh_id'] == Person_node1719078286883DF['hh_id']), "outer"), glueContext, "Join_Household_Person_node1719078578757")

job.commit()
