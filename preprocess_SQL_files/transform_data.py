from dotenv import load_dotenv
from databricks import sql
import csv
import os

# This file should take the cvs data and convert it into a database, or .db file
# performs the CREATE from CRUD operations


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
    connection = sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    )
    c = connection.cursor()

    # Drop the table if it already exists, then create a new one
    c.execute(f"DROP TABLE IF EXISTS {table_name}")
    c.execute(f"CREATE TABLE {table_name} ({table_parameters})")

    string_sql = f"INSERT INTO {table_name} VALUES"
    for i in sanitized_payload:
        string_sql += "\n" + (str(tuple(i))) + ","
    string_sql = string_sql[:-1] + ";"

    c.execute(string_sql)
    connection.commit()
    c.close()
    print(f"Successfully transformed and loaded {table_name} data!")
    return "Success"

    #     # Connect to DataBricks database
    # with sql.connect(
    #     server_hostname=os.getenv("SERVER_HOSTNAME"),
    #     http_path=os.getenv("HTTP_PATH"),
    #     access_token=os.getenv("DATABRICKS_KEY"),
    # ) as connection:

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
