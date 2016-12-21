import json

with open("rates.json") as f:
    j = json.load(f)
    ## j is a dictionary type with all of the json data in it
    ## prints the country that rates are with respet to (base)
    print(j['base'])
    ## prints the dictionary of all rates
    print(j['rates'])
    ## prints the exchange rate for a single country, relative to USD
    print(j['rates']['AUD'])
    ## print all of the countries available:
    for country in j['rates']:
        print(country)
    ## make a list of countries
    countries = [country for country in j['rates']]
    print(countries)
