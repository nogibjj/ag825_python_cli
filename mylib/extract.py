import requests


def extract(
    url="https://www.kaggle.com/datasets/erdemtaha/cancer-data/data?select=Cancer_Data.csv",
    file_path="cancer-data/data?select=Cancer_Data.csv",
):
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
