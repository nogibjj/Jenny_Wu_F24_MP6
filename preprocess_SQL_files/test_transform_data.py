from preprocess_SQL_files.transform_data import transform

"""This file takes the csv data and converts it into a database/.db file"""


def test_transform():
    """this checks to see that the transform works"""
    transform_result = transform(dataset="data/nyed_schoolscores.csv",
    table_name="jcw131_nyed_schoolscores",
    table_parameters="""
    DBN2 STRING,
    district FLOAT,
    school_name2 STRING,
    overall_grade STRING,
    overall_score FLOAT,
    progress_score FLOAT,
    progress_grade STRING,
    level STRING
    """,
    )
    
    assert transform_result == "Success"


if __name__ == "__main__":
    test_transform()
