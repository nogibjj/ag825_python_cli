import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/sqlite-lab/data/GroceryDB_IgFPro.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("CancerDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS CancerDB")
    c.execute("CREATE TABLE CancerDB (id,diagnosis)")
    # insert
    c.executemany("INSERT INTO CancerDB VALUES ( ?, ?)", payload)
    conn.commit()
    conn.close()
    return "CancerDB.db"
