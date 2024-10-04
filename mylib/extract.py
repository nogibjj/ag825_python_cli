import requests


def extract(
    file_path="Cancer_Data.csv",
):
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
