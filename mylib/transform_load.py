import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="Cancer_Data.csv"):

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("CancerDB.db")
    next(subset_data)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS CancerDB")
    c.execute("CREATE TABLE CancerDB (id,diagnosis)")
    # insert
    c.executemany("INSERT INTO CancerDB VALUES ( ?, ?)", payload)
    conn.commit()
    conn.close()
    return "CancerDB.db"
