import requests


def extract(
    url="https://github.com/nogibjj/ag825_sqlite_lab/blob/main/Cancer_Data.csv",
    file_path="Cancer_Data.csv",
):
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
