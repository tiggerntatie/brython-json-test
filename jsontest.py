import json

with open("rates.json") as f:
    j = json.load(f)
    ## j is a dictionary type with all of the json data in it
    print(j)