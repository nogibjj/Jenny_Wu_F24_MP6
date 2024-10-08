import sqlite3

from query_data import (
    query_create,
    query_read,
    query_update,
    query_delete,
    query_1,
    query_2,
)

"""This file asserts and tests all of the query functions"""


def test_query_create_1():
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
    assert result is None
    cursor.close()
    conn.close()


def test_query_create_2():
    "runs the creation of the query and asserts that it does exist"
    conn = sqlite3.connect("nypd_shooting.db")
    cursor = conn.cursor()
    expected_values = (
        2285660563456,
        "5/21/21",
        "3:33:33",
        "BRONX",
        None,
        33,
        0,
        None,
        None,
        "FALSE",
        "18-25",
        "M",
        "WHITE",
        "18-24",
        "M",
        "BLACK",
        None,
        None,
        None,
        None,
        None,
    )

    query_create(
        database="nypd_shooting.db",
        table="nypd_shooting",
        colnames="""'Incident_Key',
                'Occur_Date',
                'Occur_Time',
                'Boro',
                'Precinct',
                'Jurisdiction_Code',
                'Stat_Murder_Flag',
                'Perp_Age_Group',
                'Perp_Sex',
                'Perp_Race',
                'Vicitm_Age_Group',
                'Victim_Sex',
                'Victim_Race'
                """,
        values=""" 2285660563456,
        '5/21/21',
        '3:33:33',
        'BRONX',
        33,
        0,
        'FALSE',
        '18-25',
        'M',
        'WHITE',
        '18-24',
        'M',
        'BLACK' """,
    )
    cursor.execute(
        """
        SELECT * FROM nypd_shooting 
        WHERE Incident_Key = 2285660563456"""
    )
    result = cursor.fetchone()
    assert result == expected_values, f"Expected {expected_values} but got {result}"

    # cursor.execute(
    #     """
    #     DELETE FROM nypd_shooting
    #     WHERE Incident_Key = 2285660563456"""
    # )
    conn.commit()
    cursor.close()
    conn.close()

    print("Test passed: Entry exists in the database.")


def test_query_read():
    """testing the read function"""
    result = query_read("nypd_shooting.db", "nypd_shooting")
    assert result is not None


def test_query_update():
    """testing the update function"""
    Incident_Key = 2285660563456

    column = "Precinct"
    new_value = 35
    conn = sqlite3.connect("nypd_shooting.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Precinct FROM nypd_shooting 
        WHERE Incident_Key = 2285660563456"""
    )
    old_value = cursor.fetchone()
    query_update("nypd_shooting.db", "nypd_shooting", column, new_value, Incident_Key)
    cursor.execute(
        """
        SELECT Precinct FROM nypd_shooting 
        WHERE Incident_Key = 2285660563456"""
    )
    new_value = cursor.fetchone()
    assert new_value is not old_value
    cursor.close()
    conn.close()

    print(f"Old Value {old_value}, New Value {new_value}")


def test_delete():
    """testing the delete function"""
    conn = sqlite3.connect("nypd_shooting.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM nypd_shooting 
        WHERE Incident_Key = 2285660563456"""
    )
    presence = cursor.fetchone()

    query_delete("nypd_shooting.db", "nypd_shooting", 2285660563456)
    cursor.execute(
        """
        SELECT * FROM nypd_shooting 
        WHERE Incident_Key = 2285660563456"""
    )
    presence_1 = cursor.fetchone()
    assert presence_1 is None
    conn.commit()
    cursor.close()
    conn.close()

    print(f"{presence} has been deleted")


def test_query_1():
    result_1 = query_1(database="nypd_shooting.db", table="nypd_shooting")
    assert result_1 is not None


def test_query_2():
    result_2 = query_2(database="nypd_shooting.db", table="nypd_shooting")
    assert result_2 is not None


if __name__ == "__main__":
    test_query_create_1()
    test_query_create_2()
    test_query_read()
    test_query_update()
    test_delete()
    test_query_1()
    test_query_2()
