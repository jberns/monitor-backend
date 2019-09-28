"""
Richard Reper
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3
conn = sqlite3.connect("HeartLink_DB.db")
testDict = {
    "UID": 1,
    "FNAME": "first 1",
    "LNAME": "last 1",
    "LAT": 123,
    "LON": 345,
    "TS": "2012-04-23T18:25:43.511",
    "HR": 86,
    "BP_D": 120,
    "BP_S": 80,
    "A_SUP": 85,
    "ENV_TEMP": 200,
    "INT_TEMP": 100
  }


def send_to_server(input_dict):
    conn.execute('''
        INSERT INTO FR_DATA (UID, TS, HR, BP_D, BP_S, LAT, LON, A_SUP, ENV_TEMP, INT_TEMP, FNAME, LNAME) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (input_dict['UID'], input_dict['TS'], input_dict['HR'], input_dict['BP_D'],
              input_dict['BP_S'], input_dict['LAT'], input_dict['LON'], input_dict['A_SUP'], input_dict['ENV_TEMP'],
              input_dict['INT_TEMP'], input_dict['FNAME'], input_dict['LNAME']))
    conn.commit()
    conn.close()


def main():
    send_to_server(testDict)


main()
