"""Query the database"""

import sqlite3


def create(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO CancerDB (id,diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean)
                   VALUES (123123123, 12.312312, 12.3123312, 21.312312312, 12.3213123, 21.3123213, 23.1231312) 
                   """
    )
    cursor.execute("SELECT * FROM CancerDB WHERE id=123123123 LIMIT 5")
    print("The following record has been inserted into the database:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


def read(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CancerDB LIMIT 5")
    print("Top 5 rows of the CancerDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


def update(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(
        """ UPDATE CancerDB
                   SET diagnosis=32.12213123
                   WHERE id = 123123123
                   """
    )
    print("The following record has been modified in the database:")
    cursor.execute("SELECT * FROM CancerDB WHERE id=123123123 LIMIT 5")
    print(cursor.fetchall())
    conn.close()
    return "Success"


def delete(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(
        """ DELETE FROM CancerDB
                   WHERE id = 123123123
                   """
    )
    cursor.execute("SELECT * FROM CancerDB WHERE id=123123123 LIMIT 5")
    print(cursor.fetchall())
    conn.close()
    return "Success"


# if __name__ == "__main__":
#     create()
#     read()
#     update()
#     delete()
