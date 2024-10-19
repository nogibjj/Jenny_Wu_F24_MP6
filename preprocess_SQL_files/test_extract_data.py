import os
from extract_data import extract


"""Asserting that the Data is being extracted from the url"""


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


if __name__ == "__main__":
    test_extract()
