import json

def loadCities():
    try:
        with open('bd/cities.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except:
        return {}

def saveCities(cities):
    with open('bd/cities.json', 'w') as file:
        json.dump(cities, file)