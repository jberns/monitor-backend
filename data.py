import datetime, random

data = []

start_time = datetime.datetime(2019, 9, 28, 17, 29, 3, 191942)
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

current_time = start_time + added_time
for i in range(2000):
    
    current_time += added_time
    #print(current_time)
    #dict1 = {}
    #dict2 = {}
    #dict3 = {}
    #dict4 = {}
    #dict5 = {}

    dict1["TS"] = str(current_time)
    if i % 5 == 0:
        if dict1["HR"] < 75:
            dict1["HR"] += random.randrange(0, 2)
        elif dict1["HR"] < 160:
            dict1["HR"] += random.randrange(-1, 2)
        else:
            dict1["HR"] += random.randrange(-1, 1)
        #print(dict1["HR"])
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
    #print(dict1)
    data.append(dict1)
    for dict in data:
        if dict["UID"] == 1:
            print(dict)
    if i > 1:
        break
    if i < 20:
        print(data)
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
    data.append(dict2)

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
    data.append(dict3)

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
    data.append(dict4)

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
    data.append(dict5)


