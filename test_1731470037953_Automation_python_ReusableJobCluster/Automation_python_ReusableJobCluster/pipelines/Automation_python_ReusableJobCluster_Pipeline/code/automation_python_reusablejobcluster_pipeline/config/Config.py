from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(
            self,
            c_string: str=None,
            c_int: int=None,
            c_boolean: bool=None,
            c_short: int=None,
            c_double: float=None,
            c_float: float=None,
            c_long: int=None,
            c_spark_expression: str=None,
            **kwargs
    ):
        self.spark = None
        self.update(c_string, c_int, c_boolean, c_short, c_double, c_float, c_long, c_spark_expression)

    def update(
            self,
            c_string: str="string$$%^&*#@",
            c_int: int=65530,
            c_boolean: bool=True,
            c_short: int=2,
            c_double: float=22.0,
            c_float: float=-2.2,
            c_long: int=-2,
            c_spark_expression: str="concat('a','b')",
            **kwargs
    ):
        prophecy_spark = self.spark
        self.c_string = c_string
        self.c_int = self.get_int_value(c_int)
        self.c_boolean = self.get_bool_value(c_boolean)
        self.c_short = self.get_int_value(c_short)
        self.c_double = self.get_float_value(c_double)
        self.c_float = self.get_float_value(c_float)
        self.c_long = self.get_int_value(c_long)
        self.c_spark_expression = c_spark_expression
        pass
