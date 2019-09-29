import json

def getDict(filepath):
    jsonData = open(filepath)
    pythonObj = json.load(jsonData)
    return pythonObj

