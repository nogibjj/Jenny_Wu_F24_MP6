from query_data import (
    general_query,
)

"""This file asserts and tests all of the query functions"""


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
    expected_values = """[Row(overall_grade='A', avg_ap_test_taker=198.3235294117647), Row(overall_grade='B',
      avg_ap_test_taker=151.71052631578948), Row(overall_grade='C', avg_ap_test_taker=71.31428571428572), 
      Row(overall_grade='D', avg_ap_test_taker=55.4), Row(overall_grade='F', avg_ap_test_taker=197.6)]"""
    assert results == expected_values, f"Expected {expected_values} but got {results}"


if __name__ == "__main__":
    test_general_query()
