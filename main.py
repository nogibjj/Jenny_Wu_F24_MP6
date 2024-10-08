"""This file runs all of the query functions"""

from preprocess_SQL_files.extract_data import extract
from preprocess_SQL_files.transform_data import transform
from preprocess_SQL_files.query_data import (
    query_create,
    query_read,
    query_update,
    query_delete,
    query_1,
    query_2,
)

extract()
transform()

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
    values=""" 228566043,
                '5/03/21',
                '3:53:00',
                'BRONX',
                41,
                0,
                'FALSE',
                '18-25',
                'M',
                'WHITE HISPANIC',
                '18-24',
                'M',
                'WHITE HISPANIC'
                """,
)

query_read(database="nypd_shooting.db", table="nypd_shooting")

query_update(
    database="nypd_shooting.db",
    table="nypd_shooting",
    column="Precinct",
    new_value=78,
    Incident_Key=79853889,
)

query_delete(
    database="nypd_shooting.db", table="nypd_shooting", Incident_Key="79853889"
)

query_1(database="nypd_shooting.db", table="nypd_shooting")
query_2(database="nypd_shooting.db", table="nypd_shooting")
