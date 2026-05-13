# test-dbx-connect


Repo for testing both:
- Local testing with local spark (pyspark package)
- Testing with Databricks Connect (dbx package)


Instructions (local):
1. Setup profile for databricks connect (dbx) and test connection with `dbx test`
2. Ensure the environment variable `USE_DATABRICKS_CONNECT` is not set
3. Install local deps with `uv sync --extra local` or `pip install -e .[local]`
4. Run tests with `pytest` or whatever you need to do locally

Instructions (dbx):
1. Setup profile for databricks connect (dbx) and test connection with `dbx test`
2. Ensure the environment variable `USE_DATABRICKS_CONNECT` is set to true
3. Setup DBX connect profile within the cli using `databricks auth login --configure-cluster --host https://adb-6644860184957510.10.azuredatabricks.net/`
- this will configure the profile to use with the dev dbx workspace
4. Install dbx deps with `uv sync --extra dbx` or `pip install -e .[dbx]`