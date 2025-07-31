package io.prophecy.pipelines.automation_scala_reusablejobcluster_pipeline.config

import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(
  var c_string:           String = "string$$%^&*#@",
  var c_int:              Int = 65530,
  var c_boolean:          Boolean = true,
  var c_short:            Short = 2,
  var c_double:           Double = 22.0d,
  var c_float:            Float = -2.2f,
  var c_long:             Long = -2L,
  var c_spark_expression: String = "concat('a','b')"
) extends ConfigBase
