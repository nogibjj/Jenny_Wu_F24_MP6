"""Query the database from a db connection to Azure Databricks"""

import os
from databricks import sql
from dotenv import load_dotenv


def general_query(query):
    """runs a query a user inputs"""

    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as c:
            c.execute(query)
            result = c.fetchall()
            connection.commit()
            c.close()
        return result


result_1= general_query(
    """SELECT A.DBN1
        FROM ids706_data_engineering.default.jcw131_nyed_sat AS A
        JOIN ids706_data_engineering.default.jcw131_nyed_ap_scores AS B
        ON A.DBN1 = B.DBN2;
            """
)

print(result_1)
