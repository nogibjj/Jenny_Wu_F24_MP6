"""Query the database from a db connection to Azure Databricks"""

import os
from databricks import sql
from dotenv import load_dotenv


def general_query(query):
    """runs a query a user inputs"""

    load_dotenv()
    server_hostname_test = os.getenv("SERVER_HOSTNAME")
    http_path_test = os.getenv("DATABRICKS_HTTPPATH")
    access_token_test = os.getenv("DATABRICKS_KEY")

    # Connect to DataBricks database
    with sql.connect(
        server_hostname=server_hostname_test,
        http_path=http_path_test,
        access_token=access_token_test,
    ) as connection:

        with connection.cursor() as c:
            c.execute(query)
            result = c.fetchall()
            connection.commit()
            c.close()
    return result
