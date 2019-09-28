"""
Benjamin Stanton
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3 as sql

def getDataSnapshot():
    teamSize = 5

    conn = sql.connect("HeartLink_DB")

    conn.cursor()
    while True:
        conn.execute("SELECT " + str(teamSize) +
                     "FROM (SELECT * FROM FR_DATA ORDER BY TS desc)")
        for record in conn:
            print(record)

        break
    