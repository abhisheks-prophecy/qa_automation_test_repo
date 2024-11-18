package io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.graph

import io.prophecy.libs._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.functions.PipelineInitCode._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.functions.UDFs._
import io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object reformat_customer_data {

  def apply(context: Context, in: DataFrame): DataFrame = {
    val Config = context.config
    in.select(
      concat(lit(Config.c_string),
             lit(Config.c_int),
             lit(Config.c_boolean),
             lit(Config.c_short),
             lit(Config.c_double),
             lit(Config.c_float),
             lit(Config.c_long)
      ).as("col1"),
      expr(Config.c_spark_expression).as("col2"),
      col("customer_id"),
      col("first_name"),
      col("last_name"),
      col("phone"),
      col("email"),
      col("country_code"),
      col("account_open_date"),
      col("account_flags")
    )
  }

}
