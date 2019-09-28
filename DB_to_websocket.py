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

    columns = ["UID", "TS","HR", "BP_D", "BP_S", "LAT", "LON", "A_SUP", "ENV_TEMP", "IN_TEMP", "FNAME", "LNAME"]

    record_dict = {}

    packet = []

    for record in records:
        for i in range(len(columns)):
            record_dict[columns[i]] = record[i]
        packet.append(js.dumps(record_dict))

    return packet

data = getDataSnapshot()
serData = serializeDataSnapshot(data)




