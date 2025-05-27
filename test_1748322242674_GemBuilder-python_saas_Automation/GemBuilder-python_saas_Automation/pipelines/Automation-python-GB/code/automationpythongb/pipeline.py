from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automationpythongb.config.ConfigStore import *
from automationpythongb.functions import *
from prophecy.utils import *
from automationpythongb.graph import *

def pipeline(spark: SparkSession) -> None:
    df_GB_TestDataset = GB_TestDataset(spark)
    df_customer_details_selection = customer_details_selection(spark, df_GB_TestDataset)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("Automation-python-GB").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Automation-python-GB")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Automation-python-GB", config = Config)(pipeline)

if __name__ == "__main__":
    main()
