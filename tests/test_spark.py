from src.config import UDataFrame


def test_spark_test_one(spark):
    df: UDataFrame  = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
    assert df.count() == 2


def test_spark_test_two(spark):
    df: UDataFrame = spark.createDataFrame([(3, "Charlie"), (4, "David")], ["id", "name"])
    assert df.count() == 3

