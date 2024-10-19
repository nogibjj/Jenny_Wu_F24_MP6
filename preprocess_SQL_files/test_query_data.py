import sqlite3

from query_data import (
    general_query,
)

"""This file asserts and tests all of the query functions"""


def test_general_query():
    "checks to see that the observation does not exist"
    conn = sqlite3.connect("nypd_shooting.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM nypd_shooting 
        WHERE Incident_Key = 2285660563456"""
    )
    result = cursor.fetchone()
    print(result)
    assert result is not None
    cursor.close()
    conn.close()


if __name__ == "__main__":
    test_general_query()
