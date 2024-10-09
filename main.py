""""This file runs all of the query functions"""

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

# Extracts the first data set on historic NYPD shooting incident data; saves it as a .csv
extract()

# Transforms the first data set into a .db
transform(
    dataset="data/nypd_shooting.csv",
    db_name="nypd_shooting.db",
    table_name="nypd_shooting",
    table_values="""
                Incident_Key INTEGER,
                Occur_Date TEXT,
                Occur_Time TEXT, 
                Boro TEXT,
                Loc_of_occur_desc TEXT, 
                Precinct NUMBER,
                Jurisdiction_Code INTEGER,
                Location_Class_Desc TEXT,
                Loc_Desc TEXT,
                Stat_Murder_Flag BOOL,
                Perp_Age_Group TEXT,
                Perp_Sex TEXT,
                Perp_Race TEXT,
                Vicitm_Age_Group TEXT,
                Victim_Sex TEXT,
                Victim_Race TEXT,
                X_Coord TEXT,
                Y_Coord TEXT,
                Latitide_Coord FLOAT,
                Longitude_Coord FLOAT,
                Long_Lat FLOAT""",
    num_variables=21,
)

# Creates a table in the .db to store all data
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

# Extracts the second data set on historic NYPD arrest data; saves it as a .csv
extract("https://data.cityofnewyork.us/resource/8h9b-rp9u.csv", "data/nypd_arrests.csv")

# Transforms the second data set into a .db
transform(
    "data/nypd_arrests.csv",
    "nypd_arrests.db",
    "nypd_arrests",
    """
          arrest_key INTEGER,
          arrest_date TEXT, 
          pd_cd INTEGER, 
          pd_desc TEXT, 
          ky_cd INTEGER, 
          ofns_desc TEXT, 
          law_code TEXT, 
          law_cat_cd TEXT, 
          arrest_boro TEXT, 
          arrest_precinct INTEGER, 
          jurisdiction_code INTEGER, 
          age_group TEXT, 
          perp_sex TEXT, 
          perp_race TEXT, 
          x_coord_cd INTEGER, 
          y_coord_cd INTEGER, 
          latitude FLOAT, 
          longitude FLOAT, 
          lon_lat TEXT""",
    19,
)


"insert function for join"
"insert function for aggregate"
"insert function for sorting "