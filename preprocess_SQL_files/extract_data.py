import requests

"""
Extract a dataset from a URL and place it into a database
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
