from src.config import get_spark_session, USparkSession
import pytest


@pytest.fixture(scope="session")
def spark() -> USparkSession:
    return get_spark_session(dbx_profile="dbx-connect-test")