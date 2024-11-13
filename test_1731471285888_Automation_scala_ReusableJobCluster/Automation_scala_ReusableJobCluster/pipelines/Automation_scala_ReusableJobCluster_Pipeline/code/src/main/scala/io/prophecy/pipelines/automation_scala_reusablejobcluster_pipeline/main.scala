package io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline

import io.prophecy.libs._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.config._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.functions.UDFs._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.functions.PipelineInitCode._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_dataset_cust_in = dataset_cust_in(context)
    val df_reformat_customer_data =
      reformat_customer_data(context, df_dataset_cust_in)
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.getConfig(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Automation_scala_ReusableJobCluster_Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
    val context = Context(spark, config)
    spark.conf.set("prophecy.metadata.pipeline.uri",
                   "pipelines/Automation_scala_ReusableJobCluster_Pipeline"
    )
    registerUDFs(spark)
    MetricsCollector.instrument(
      spark,
      "pipelines/Automation_scala_ReusableJobCluster_Pipeline"
    ) {
      apply(context)
    }
  }

}
