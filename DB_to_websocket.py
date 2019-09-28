"""
Benjamin Stanton
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3 as sql

def getDataSnapshot():
    teamSize = 1

    conn = sql.connect("HeartLink_DB.db")

    conn.cursor()
    while True:

        for record in conn.execute("SELECT " + str(teamSize) +
                     " FROM (SELECT * FROM FR_DATA ORDER BY TS desc);"):
            print(record)
        break


getDataSnapshot()
