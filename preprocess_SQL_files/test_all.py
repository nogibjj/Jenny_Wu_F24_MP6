import os
from databricks import sql
from dotenv import load_dotenv
from preprocess_SQL_files.extract_data import extract
from preprocess_SQL_files.transform_data import transform
from preprocess_SQL_files.query_data import general_query


def test_extract():
    """this extracts the data from a URL and puts it into a CSV files"""
    result = extract(
        """https://data.cityofnewyork.us/resource/itfs-ms3e.csv?$query=
                     SELECT%0A%20%20%60dbn%60%2C%0A%20%20%60schoolname%60%2C%0A%20%2
                     0%60ap_test_takers_%60%2C%0A%20%20%60total_exams_
                     taken%60%2C%0A%20%20%60number_of_exams_with_scores_3_4_or_5%60%0AWHERE
                     %20%60number_of_exams_with_scores_3_4_or_5%60%20IS%20NOT%20NULL""",
        "data/nyed_ap_scores.csv",
    )
    assert os.path.exists(result)


def test_transform():
    """this checks to see that the transform works"""
    transform_result = transform(
        dataset="data/nyed_schoolscores.csv",
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


def test_general_query():
    "checks to see that it returns a result"
    results = general_query(
        """SELECT overall_grade, AVG(ap_test_taker) AS avg_ap_test_taker
        FROM ids706_data_engineering.default.jcw131_nyed_ap_score
        JOIN ids706_data_engineering.default.jcw131_nyed_schoolscores
        ON jcw131_nyed_ap_score.DBN2 = jcw131_nyed_schoolscores.DBN2
        GROUP BY overall_grade
        ORDER BY overall_grade;"""
    )
    results = str(results)
    expected_values = """[Row(overall_grade='A', avg_ap_test_taker=198.3235294117647), 
    Row(overall_grade='B', avg_ap_test_taker=151.71052631578948), 
    Row(overall_grade='C', avg_ap_test_taker=71.31428571428572), 
    Row(overall_grade='D', avg_ap_test_taker=55.4), 
    Row(overall_grade='F', avg_ap_test_taker=197.6)]"""
    assert results == expected_values, f"Expected {expected_values} but got {results}"


if __name__ == "__main__":
    test_extract()
    test_transform()
    test_general_query()
