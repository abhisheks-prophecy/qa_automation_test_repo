from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automation_python_reusablejobcluster_pipeline.config.ConfigStore import *
from automation_python_reusablejobcluster_pipeline.functions import *

def reformatted_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(
            lit(Config.c_string), 
            lit(Config.c_int), 
            lit(Config.c_boolean), 
            lit(Config.c_short), 
            lit(Config.c_double), 
            lit(Config.c_float), 
            lit(Config.c_long)
          )\
          .alias("col1"), 
        expr(Config.c_spark_expression).alias("col2"), 
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        col("email"), 
        col("country_code"), 
        col("account_open_date"), 
        col("account_flags")
    )
