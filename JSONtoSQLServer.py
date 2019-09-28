"""
Richard Reper
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3
import datetime
conn = sqlite3.connect("HeartLink_DB.db")
while True:
    TimeVar = str(datetime.datetime.now())
    conn.execute('''
        INSERT INTO FR_DATA (UID, TS, HR, BP_D, BP_S, LAT, LON, A_SUP, ENV_TEMP, INT_TEMP, FNAME, LNAME) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (0, TimeVar[0:23], 80, 0, 0, 0, 0, 0, 0, 0, 'Jon', 'Smith'))
    conn.commit()
    exit()
conn.close()