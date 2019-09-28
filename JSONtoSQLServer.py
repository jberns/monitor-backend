"""
Richard Reper
Tech2Protect Denver
HeartLink
9/28/19
"""

import sqlite3
conn = sqlite3.connect("HeartLink_DB.db")


def send_to_server(input_dict):
    conn.execute('''
        INSERT INTO FR_DATA (UID, TS, HR, BP_D, BP_S, LAT, LON, A_SUP, ENV_TEMP, INT_TEMP, FNAME, LNAME) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (input_dict['UID'], input_dict['TS'], input_dict['HR'], input_dict['BP_D'], input_dict['BP_S'], input_dict['LAT'], input_dict['LON'], input_dict['A_SUP'], input_dict['ENV_TEMP'], input_dict['INT_TEMP'], input_dict['FNAME'], input_dict['LNAME']))
    conn.commit()
    conn.close()

def main():
    
