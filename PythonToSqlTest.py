"""
Richard Reper
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3
import datetime
conn = sqlite3.connect("HeartLink_DB.db")
"""conn.execute('''
    CREATE TABLE FR_DATA (
    UID      INTEGER,
    TS       TIME,
    HR       INTEGER,
    BP_D     INTEGER,
    BP_S     INTEGER,
    LAT      DOUBLE,
    LON      DOUBLE,
    A_SUP    INTEGER,
    ENV_TEMP INTEGER,
    INT_TEMP INTEGER,
    FNAME    STRING,
    LNAME    STRING,
    PRIMARY KEY (UID, TS)
);
''')"""
TimeVar = str(datetime.datetime.now())
conn.execute('''
    INSERT INTO FR_DATA (UID, TS, FNAME, LNAME) VALUES (?, ?, ?, ?);
''', (0, TimeVar[10:19], 'Jon', 'Smith'))
conn.commit()
conn.close()



