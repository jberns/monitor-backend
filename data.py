import datetime, random

data = []

start_time = datetime.datetime.now()#(2019, 9, 28, 17, 29, 3, 191942)
added_time = datetime.timedelta(0, 0, 500000)

dict1 = {
    "UID": 1,
    "FNAME": "John",
    "LNAME": "Smith",
    "TS": str(start_time),
    "LAT": 39.732431,
    "LON": -104.966825,
    "A_SUP": 100,
    "ENV_TEMP": 80,
    "INT_TEMP": 98,
    "HR": 85,
    "BP_D": 70,
    "BP_S": 100,
}
dict2 = {
    "UID": 2,
    "FNAME": "Mary",
    "LNAME": "Fletcher",
    "TS": str(start_time),
    "LAT": 39.730431,
    "LON": -104.967825,
    "A_SUP": 100,
    "ENV_TEMP": 80,
    "INT_TEMP": 98,
    "HR": 100,
    "BP_D": 65,
    "BP_S": 120,
}
dict3 = {
    "UID": 3,
    "FNAME": "Jose",
    "LNAME": "Rodriguez",
    "TS": str(start_time),
    "LAT": 39.731231,
    "LON": -104.965225,
    "A_SUP": 100,
    "ENV_TEMP": 80,
    "INT_TEMP": 98,
    "HR": 90,
    "BP_D": 82,
    "BP_S": 135,
}
dict4 = {
    "UID": 4,
    "FNAME": "Alice",
    "LNAME": "Jones",
    "TS": str(start_time),
    "LAT": 39.732431,
    "LON": -104.966765,
    "A_SUP": 100,
    "ENV_TEMP": 80,
    "INT_TEMP": 98,
    "HR": 130,
    "BP_D": 90,
    "BP_S": 140,
}
dict5 = {
    "UID": 5,
    "FNAME": "Bill",
    "LNAME": "Collins",
    "TS": str(start_time),
    "LAT": 39.732231,
    "LON": -104.967025,
    "A_SUP": 100,
    "ENV_TEMP": 80,
    "INT_TEMP": 98,
    "HR": 120,
    "BP_D": 85,
    "BP_S": 120,
}

data.append(dict1)
data.append(dict2)
data.append(dict3)
data.append(dict4)
data.append(dict5)




tempDict = {}
current_time = start_time + added_time
for i in range(2000):
    current_time += added_time

    dict1["TS"] = str(current_time)
    if i % 5 == 0:
        if dict1["HR"] < 75:
            dict1["HR"] += random.randrange(0, 2)
        elif dict1["HR"] < 160:
            dict1["HR"] += random.randrange(-1, 2)
        else:
            dict1["HR"] += random.randrange(-1, 1)

    if dict1["A_SUP"] > 0:
        if i % 20 == 0:
            dict1["A_SUP"] -= random.randrange(0, 2)
    if i % 2 == 0:
        dict1["ENV_TEMP"] += random.randrange(0, 2)
    if i % 100 == 0:
        dict1["INT_TEMP"] += random.randrange(0, 2)
    dict1["LAT"] += random.uniform(-1, 1) * .0001
    dict1["LON"] += random.uniform(-1, 1) * .0001
    if i % 1 == 0:
        if dict1["BP_D"] < 60:
            dict1["BP_D"] += random.randrange(0, 2)
        elif dict1["BP_D"] < 80:
            dict1["BP_D"] += random.randrange(-1, 2)
        else:
            dict1["BP_D"] += random.randrange(-1, 1)
    if i % 1 == 0:
        if dict1["BP_S"] < 90:
            dict1["BP_S"] += random.randrange(0, 2)
        elif dict1["BP_S"] < 120:
            dict1["BP_S"] += random.randrange(-1, 2)
        else:
            dict1["BP_S"] += random.randrange(-1, 1)
    tempDict["UID"] = dict1["UID"]
    tempDict["FNAME"] = dict1["FNAME"]
    tempDict["LNAME"] = dict1["LNAME"]
    tempDict["TS"] = dict1["TS"]
    tempDict["LAT"] = dict1["LAT"]
    tempDict["LON"] = dict1["LON"]
    tempDict["A_SUP"] = dict1["A_SUP"]
    tempDict["ENV_TEMP"] = dict1["ENV_TEMP"]
    tempDict["INT_TEMP"] = dict1["INT_TEMP"]
    tempDict["HR"] = dict1["HR"]
    tempDict["BP_D"] = dict1["BP_D"]
    tempDict["BP_S"] = dict1["BP_S"]
    data.append(tempDict)
    tempDict = {}

    dict2["TS"] = str(current_time)
    if i % 1 == 0:
        if dict2["HR"] < 75:
            dict2["HR"] += random.randrange(0, 2)
        elif dict2["HR"] < 160:
            dict2["HR"] += random.randrange(-1, 2)
        else:
            dict2["HR"] += random.randrange(-1, 1)
    if dict2["A_SUP"] > 0:
        if i % 20 == 0:
            dict2["A_SUP"] -= random.randrange(0, 2)
    if i % 2 == 0:
        dict2["ENV_TEMP"] += random.randrange(0, 2)
    if i % 100 == 0:
        dict2["INT_TEMP"] += random.randrange(0, 2)
    dict2["LAT"] += random.uniform(-1, 1) * .0001
    dict2["LON"] += random.uniform(-1, 1) * .0001
    if i % 1 == 0:
        if dict2["BP_D"] < 60:
            dict2["BP_D"] += random.randrange(0, 2)
        elif dict2["BP_D"] < 80:
            dict2["BP_D"] += random.randrange(-1, 2)
        else:
            dict2["BP_D"] += random.randrange(-1, 1)
    if i % 1 == 0:
        if dict2["BP_S"] < 90:
            dict2["BP_S"] += random.randrange(0, 2)
        elif dict2["BP_S"] < 120:
            dict2["BP_S"] += random.randrange(-1, 2)
        else:
            dict2["BP_S"] += random.randrange(-1, 1)
    tempDict["UID"] = dict2["UID"]
    tempDict["FNAME"] = dict2["FNAME"]
    tempDict["LNAME"] = dict2["LNAME"]
    tempDict["TS"] = dict2["TS"]
    tempDict["LAT"] = dict2["LAT"]
    tempDict["LON"] = dict2["LON"]
    tempDict["A_SUP"] = dict2["A_SUP"]
    tempDict["ENV_TEMP"] = dict2["ENV_TEMP"]
    tempDict["INT_TEMP"] = dict2["INT_TEMP"]
    tempDict["HR"] = dict2["HR"]
    tempDict["BP_D"] = dict2["BP_D"]
    tempDict["BP_S"] = dict2["BP_S"]
    data.append(tempDict)
    tempDict = {}


    dict3["TS"] = str(current_time)
    if i % 1 == 0:
        if dict3["HR"] < 75:
            dict3["HR"] += random.randrange(0, 2)
        elif dict3["HR"] < 160:
            dict3["HR"] += random.randrange(-1, 2)
        else:
            dict3["HR"] += random.randrange(-1, 1)
    if dict3["A_SUP"] > 0:
        if i % 20 == 0:
            dict3["A_SUP"] -= random.randrange(0, 2)
    if i % 2 == 0:
        dict3["ENV_TEMP"] += random.randrange(0, 2)
    if i % 100 == 0:
        dict3["INT_TEMP"] += random.randrange(0, 2)
    dict3["LAT"] += random.uniform(-1, 1) * .0001
    dict3["LON"] += random.uniform(-1, 1) * .0001
    if i % 1 == 0:
        if dict3["BP_D"] < 60:
            dict3["BP_D"] += random.randrange(0, 2)
        elif dict3["BP_D"] < 80:
            dict3["BP_D"] += random.randrange(-1, 2)
        else:
            dict3["BP_D"] += random.randrange(-1, 1)
    if i % 1 == 0:
        if dict3["BP_S"] < 90:
            dict3["BP_S"] += random.randrange(0, 2)
        elif dict3["BP_S"] < 120:
            dict3["BP_S"] += random.randrange(-1, 2)
        else:
            dict3["BP_S"] += random.randrange(-1, 1)
    tempDict["UID"] = dict3["UID"]
    tempDict["FNAME"] = dict3["FNAME"]
    tempDict["LNAME"] = dict3["LNAME"]
    tempDict["TS"] = dict3["TS"]
    tempDict["LAT"] = dict3["LAT"]
    tempDict["LON"] = dict3["LON"]
    tempDict["A_SUP"] = dict3["A_SUP"]
    tempDict["ENV_TEMP"] = dict3["ENV_TEMP"]
    tempDict["INT_TEMP"] = dict3["INT_TEMP"]
    tempDict["HR"] = dict3["HR"]
    tempDict["BP_D"] = dict3["BP_D"]
    tempDict["BP_S"] = dict3["BP_S"]
    data.append(tempDict)
    tempDict = {}


    dict4["TS"] = str(current_time)
    if i % 1 == 0:
        if dict4["HR"] < 75:
            dict4["HR"] += random.randrange(0, 2)
        elif dict4["HR"] < 160:
            dict4["HR"] += random.randrange(-1, 2)
        else:
            dict4["HR"] += random.randrange(-1, 1)
    if dict4["A_SUP"] > 0:
        if i % 20 == 0:
            dict4["A_SUP"] -= random.randrange(0, 2)
    if i % 2 == 0:
        dict4["ENV_TEMP"] += random.randrange(0, 2)
    if i % 100 == 0:
        dict4["INT_TEMP"] += random.randrange(0, 2)
    dict4["LAT"] += random.uniform(-1, 1) * .0001
    dict4["LON"] += random.uniform(-1, 1) * .0001
    if i % 1 == 0:
        if dict4["BP_D"] < 60:
            dict4["BP_D"] += random.randrange(0, 2)
        elif dict4["BP_D"] < 80:
            dict4["BP_D"] += random.randrange(-1, 2)
        else:
            dict4["BP_D"] += random.randrange(-1, 1)
    if i % 1 == 0:
        if dict4["BP_S"] < 90:
            dict4["BP_S"] += random.randrange(0, 2)
        elif dict4["BP_S"] < 120:
            dict4["BP_S"] += random.randrange(-1, 2)
        else:
            dict4["BP_S"] += random.randrange(-1, 1)
    tempDict["UID"] = dict4["UID"]
    tempDict["FNAME"] = dict4["FNAME"]
    tempDict["LNAME"] = dict4["LNAME"]
    tempDict["TS"] = dict4["TS"]
    tempDict["LAT"] = dict4["LAT"]
    tempDict["LON"] = dict4["LON"]
    tempDict["A_SUP"] = dict4["A_SUP"]
    tempDict["ENV_TEMP"] = dict4["ENV_TEMP"]
    tempDict["INT_TEMP"] = dict4["INT_TEMP"]
    tempDict["HR"] = dict4["HR"]
    tempDict["BP_D"] = dict4["BP_D"]
    tempDict["BP_S"] = dict4["BP_S"]
    data.append(tempDict)
    tempDict = {}


    dict5["TS"] = str(current_time)
    if i % 1 == 0:
        if dict5["HR"] < 75:
            dict5["HR"] += random.randrange(0, 2)
        elif dict5["HR"] < 160:
            dict5["HR"] += random.randrange(-1, 2)
        else:
            dict5["HR"] += random.randrange(-1, 1)
    if dict5["A_SUP"] > 0:
        if i % 20 == 0:
            dict5["A_SUP"] -= random.randrange(0, 2)
    if i % 2 == 0:
        dict5["ENV_TEMP"] += random.randrange(0, 2)
    if i % 100 == 0:
        dict5["INT_TEMP"] += random.randrange(0, 2)
    dict5["LAT"] += random.uniform(-1, 1) * .0001
    dict5["LON"] += random.uniform(-1, 1) * .0001
    if i % 1 == 0:
        if dict5["BP_D"] < 60:
            dict5["BP_D"] += random.randrange(0, 2)
        elif dict5["BP_D"] < 80:
            dict5["BP_D"] += random.randrange(-1, 2)
        else:
            dict5["BP_D"] += random.randrange(-1, 1)
    if i % 1 == 0:
        if dict5["BP_S"] < 90:
            dict5["BP_S"] += random.randrange(0, 2)
        elif dict5["BP_S"] < 120:
            dict5["BP_S"] += random.randrange(-1, 2)
        else:
            dict5["BP_S"] += random.randrange(-1, 1)
    tempDict["UID"] = dict5["UID"]
    tempDict["FNAME"] = dict5["FNAME"]
    tempDict["LNAME"] = dict5["LNAME"]
    tempDict["TS"] = dict5["TS"]
    tempDict["LAT"] = dict5["LAT"]
    tempDict["LON"] = dict5["LON"]
    tempDict["A_SUP"] = dict5["A_SUP"]
    tempDict["ENV_TEMP"] = dict5["ENV_TEMP"]
    tempDict["INT_TEMP"] = dict5["INT_TEMP"]
    tempDict["HR"] = dict5["HR"]
    tempDict["BP_D"] = dict5["BP_D"]
    tempDict["BP_S"] = dict5["BP_S"]
    data.append(tempDict)
    tempDict = {}
for i in range(5):
    data.remove(data[0])

f = open('C:\\Users\\richie\\Documents\\GitHub\\T2P-challenge-7-backend\\demonstration_data', 'w')
for dict_iteratable in data:
    f.write(str(dict_iteratable))
    f.write('\n')
f.close()