from config import get_spark_session
import os
# run on dbx


def dbx_function_for_testing():
    os.environ["USE_DATABRICKS_CONNECT"] = "true"
    spark = get_spark_session("dbx-connect-test")
    df = spark.read.table("retail_operations_dev.work_mins.rdf_raw")
    df.printSchema()
    df.show(n=5)

if __name__ == "__main__":
    dbx_function_for_testing()