from dotenv import load_dotenv
from databricks import sql
import csv
import os

# This file should take the cvs data and convert it into a database, or .db file


# Loads the CSV file and transforms it into a new SQLite3 database
def transform(dataset, table_name, table_parameters):
    """Transforms and Loads data into the local SQLite3 database"""
    load_dotenv()
    # Open the CSV file
    with open(dataset, newline="", encoding="ISO-8859-1") as csvfile:
        payload = csv.reader(csvfile, delimiter=",")
        next(payload)
        sanitized_payload = [
            tuple(map(lambda x: x.strip() if isinstance(x, str) else x, row))
            for row in payload
        ]

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
            c.execute(f"SELECT * FROM {table_name}")
            result = c.fetchall()
            if not result:
                # Drop the table if it already exists, then create a new one
                c.execute(f"DROP TABLE IF EXISTS {table_name}")
                c.execute(f"CREATE TABLE {table_name} ({table_parameters})")

                string_sql = f"INSERT INTO {table_name} VALUES"
                for i in sanitized_payload:
                    string_sql += "\n" + (str(tuple(i))) + ","
                string_sql = string_sql[:-1] + ";"
                print(string_sql)

                c.execute(string_sql)
                connection.commit()
                c.close()
                print(f"Successfully transformed and loaded {table_name} data!")
    return "Success"


# OLD CODE
#     # Connect to DataBricks database
# with sql.connect(
#     server_hostname=os.getenv("SERVER_HOSTNAME"),
#     http_path=os.getenv("DATABRICKS_HTTPPATH"),
#     access_token=os.getenv("DATABRICKS_KEY")) as connection:

#     with connection.cursor() as c:

#         # Drop the table if it already exists, then create a new one
#         c.execute(f"DROP TABLE IF EXISTS {table_name}")
#         c.execute(f"CREATE TABLE {table_name} ({table_parameters})")

#         string_sql = f"INSERT INTO {table_name} VALUES"
#         for i in sanitized_payload:
#             string_sql += "\n" + (str(tuple(i))) + ","
#         string_sql = string_sql[:-1] + ";"

#         c.execute(string_sql)
#         connection.commit()
#         c.close()
#         print(f"Successfully transformed and loaded {table_name} data!")
#     return "Success"

