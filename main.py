from preprocess_SQL_files.extract_data import extract
from preprocess_SQL_files.transform_data import transform
from preprocess_SQL_files.query_data import general_query

extract(
    """https://data.cityofnewyork.us/resource/itfs-ms3e.csv?$query=SELECT
       %0A%20%20%60dbn%60%2C%0A%20%20%60schoolname%60%2C%0A%20%20%60ap_test_takers_
      %60%2C%0A%20%20%60total_exams_taken%60%2C%0A%20%20%60number_of_exams_with_scores_3_4_or_5
      %60%0AWHERE%20%60number_of_exams_with_scores_3_4_or_5%60%20IS%20NOT%20NULL""",
    "data/nyed_ap_scores.csv",
)

extract(
    """https://data.cityofnewyork.us/resource/upwt-zvh3.csv?$query=SELECT
      %0A%20%20%60dbn%60%2C%0A%20%20%60district%60%2C%0A%20%20%60school
      %60%2C%0A%20%20%60_2010_2011_overall_grade%60%2C%0A%20%20%60_2010_2011_overall_score
      %60%2C%0A%20%20%60_2010_2011_progress_category_score%60%2C%0A%20%20%60_2010_2011_
      progress_grade%60%2C%0A%20%20%60school_level%60%0AWHERE%20%60_2010_2011_overall_grade
      %60%20IS%20NOT%20NULL""",
    "data/nyed_schoolscores.csv",
)

transform(
    dataset="data/nyed_ap_scores.csv",
    table_name="jcw131_nyed_ap_score",
    table_parameters="""
    DBN2 STRING,
    school_name1 STRING,
    ap_test_taker INTEGER,
    total_exams INTEGER,
    exams_plus INTEGER
    """,
)

transform(
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

result_1 = general_query(
    """SELECT overall_grade, AVG(ap_test_taker) AS avg_ap_test_taker
        FROM ids706_data_engineering.default.jcw131_nyed_ap_score
        JOIN ids706_data_engineering.default.jcw131_nyed_schoolscores
        ON jcw131_nyed_ap_score.DBN2 = jcw131_nyed_schoolscores.DBN2
        GROUP BY overall_grade
        ORDER BY overall_grade;
        """
)

print(result_1)
