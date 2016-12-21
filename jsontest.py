import json

with open("rates.json") as f:
    j = json.load(f)
    ## j is a dictionary type with all of the json data in it
    for x in j:
        print(x)
    for x in j['list']:
        print(x)
    #for x in j['list']['resources']:

    #print(j['list']['meta'])
    #print(j['list']['resources'])
    print(type(j['list']['resources'])
