"""Query the database"""

import sqlite3


def query():
    conn = sqlite3.connect("CancerDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CancerDB LIMIT 5")
    print("Top 5 rows of the CancerDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
