from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create
from mylib.query import read
from mylib.query import update
from mylib.query import delete

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/nogibjj/ag825_sqlite_lab/refs/heads/main/Cancer_Data.csv"
    file_path = "Cancer_Data.csv"
    database = "CancerDB.db"

    # Extract
    print("Extracting data...")
    extract(url, file_path)

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    print("Querying data...")
    create(database)
    read(database)
    # update(database)
    # delete(database)
