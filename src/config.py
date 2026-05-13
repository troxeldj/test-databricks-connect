import os

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame as LocalDataFrame
from pyspark.sql.connect.dataframe import DataFrame as ConnectDataFrame

try:
    from databricks.connect import DatabricksSession
except ImportError:
    DatabricksSession = None  # type: ignore

type UDataFrame = LocalDataFrame | ConnectDataFrame
type USparkSession = DatabricksSession | SparkSession

def get_spark_session(dbx_profile: str = None) -> USparkSession:
    USE_DATABRICKS_CONNECT: bool = os.getenv("USE_DATABRICKS_CONNECT", "false").lower() == "true"
    if USE_DATABRICKS_CONNECT:
        if DatabricksSession is None:
            raise RuntimeError(
                "USE_DATABRICKS_CONNECT=true but databricks-connect is not installed"
            )
        builder: DatabricksSession.Builder = DatabricksSession.builder
        if dbx_profile:
            builder = builder.profile(dbx_profile)
        return builder.getOrCreate()
    return SparkSession.builder.master("local[*]").appName("test").getOrCreate()