import requests

"""
Extract a dataset from a URL and place it into a database

NYPD Shooting dataset
"""


def extract(
    url,
    file_path,
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


extract(
    "https://data.cityofnewyork.us/resource/zt9s-n5aj.csv?$query=SELECT%0A%20%20%60dbn%60%2C%0A%20%20%60school_name%60%2C%0A%20%20%60number_of_test_takers%60%2C%0A%20%20%60critical_reading_mean%60%2C%0A%20%20%60mathematics_mean%60%2C%0A%20%20%60writing_mean%60%0AWHERE%20%60critical_reading_mean%60%20IS%20NOT%20NULL",
    "data/nyed_sat.csv",
)
extract(
    "https://data.cityofnewyork.us/resource/itfs-ms3e.csv?$query=SELECT%0A%20%20%60dbn%60%2C%0A%20%20%60schoolname%60%2C%0A%20%20%60ap_test_takers_%60%2C%0A%20%20%60total_exams_taken%60%2C%0A%20%20%60number_of_exams_with_scores_3_4_or_5%60%0AWHERE%20%60number_of_exams_with_scores_3_4_or_5%60%20IS%20NOT%20NULL",
    "data/nyed_ap_scores.csv",
)
