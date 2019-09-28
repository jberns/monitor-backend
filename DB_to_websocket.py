"""
Benjamin Stanton
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3 as sql
import json as js

def getDataSnapshot():

    teamSize = 5

    records = []

    conn = sql.connect("HeartLink_DB.db")

    conn.cursor()



    for record in conn.execute("SELECT * FROM FR_DATA ORDER BY TS desc LIMIT " + str(teamSize) + ";"):
        records.append(record)

    return records

def serializeDataSnapshot(records):

    packet = []

    for record in records:
        packet.append(js.dumps(record))

    print(packet)

    return packet

data = getDataSnapshot()
serData = serializeDataSnapshot(data)




