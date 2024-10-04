import sqlite3
import csv
import os


def load(
    dataset=r"C:\Users\asus\Desktop\DUKE\STUDIES\FALL 2024\IDS 706 - Data Engineering Systems\ag825_sqlite_lab\Cancer_Data.csv",
):

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("Cancer_Data.csv")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS CancerDB")
    c.execute(
        "CREATE TABLE CancerDB (id,diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean)"
    )
    # insert
    c.executemany("INSERT INTO CancerDB VALUES ( ?, ?,?,?,?,?,?)", payload)
    conn.commit()
    conn.close()
    return "CancerDB.db"
