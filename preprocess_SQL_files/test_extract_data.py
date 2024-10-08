import os
from extract_data import extract


"""Asserting that the Data is being extracted from the url"""


def test_extract():
    url = (
        "https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD"
    )
    file_path = "data/nypd_shooting.csv"
    result = extract(url, file_path)
    assert os.path.exists(result)


if __name__ == "__main__":
    test_extract()
