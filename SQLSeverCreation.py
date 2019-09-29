"""
Richard Reper
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3
conn = sqlite3.connect("HeartLink_DB.db")
conn.execute('DROP TABLE FR_DATA;')
conn.execute('''
    CREATE TABLE FR_DATA (
    UID      INTEGER,
    TS       DATETIME,
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
''')




