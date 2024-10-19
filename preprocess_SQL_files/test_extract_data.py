import os
from extract_data import extract


"""Asserting that the Data is being extracted from the url"""

url = "https://data.cityofnewyork.us/resource/833y-fsy8.csv?$query=SELECT%0A%20%20%60incident_key%60%2C%0A%20%20%60occur_date%60%2C%0A%20%20%60occur_time%60%2C%0A%20%20%60boro%60%2C%0A%20%20%60precinct%60%2C%0A%20%20%60jurisdiction_code%60%2C%0A%20%20%60statistical_murder_flag%60%2C%0A%20%20%60perp_age_group%60%2C%0A%20%20%60perp_sex%60%2C%0A%20%20%60perp_race%60%2C%0A%20%20%60vic_age_group%60%2C%0A%20%20%60vic_sex%60%2C%0A%20%20%60vic_race%60%0AWHERE%0A%20%20%60occur_date%60%0A%20%20%20%20BETWEEN%20%222006-01-01T19%3A22%3A56%22%20%3A%3A%20floating_timestamp%0A%20%20%20%20AND%20%222006-12-31T19%3A22%3A56%22%20%3A%3A%20floating_timestamp"
file_path = "data/nypd_shooting.csv"


def test_extract(url, file_path):
    result = extract(url, file_path)
    assert os.path.exists(result)


if __name__ == "__main__":
    test_extract()
