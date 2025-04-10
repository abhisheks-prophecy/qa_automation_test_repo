package io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
