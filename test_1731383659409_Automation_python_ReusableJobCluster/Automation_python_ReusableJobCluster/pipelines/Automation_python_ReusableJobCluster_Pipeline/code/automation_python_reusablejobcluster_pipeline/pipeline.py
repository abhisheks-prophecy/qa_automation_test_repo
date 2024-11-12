from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automation_python_reusablejobcluster_pipeline.config.ConfigStore import *
from automation_python_reusablejobcluster_pipeline.functions import *
from prophecy.utils import *
from automation_python_reusablejobcluster_pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset_cust_in = dataset_cust_in(spark)
    df_reformatted_columns = reformatted_columns(spark, df_dataset_cust_in)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Automation_python_ReusableJobCluster_Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Automation_python_ReusableJobCluster_Pipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(
        spark = spark,
        pipelineId = "pipelines/Automation_python_ReusableJobCluster_Pipeline",
        config = Config
    )(
        pipeline
    )

if __name__ == "__main__":
    main()
