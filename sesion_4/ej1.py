import random

names = ["Ana", "Beto", "Carlos", "Daniel", "Edna", "Fatima", "Gerardo"]
lasts = ["Alvarez", "Benitez", "Castillo", "Diaz", "Escamilla", "Fernandez"]

fullnames = []

# Make a list of fake data
for i in range(100):
    n = random.choice(names) # Choose randomly an element
    l = random.choice(lasts)

    s = "%s %s" % (n, l)

    fullnames.append(s)

print fullnames

people = []

genders = ["Male", "Female", "Not defined"]
streets = ["Rojo Gomez", "Reforma", "Bicentenario", "Juarez"]
neighborhoods = ["Condesa", "Roma Norte", "Narvarte"]

for name in fullnames:
    # Single dictionary with the person information
    d = {
        "name": name, # In the "name" key, storage the <name> value
        "age": random.randint(0, 80), # Generate a random value between 0 and 80
        "gender": random.choice(genders),
        "address": {
            "street": random.choice(streets),
            "number": random.randint(1, 400),
            "neighborhood": random.choice(neighborhoods),
            "city": "Mexico City",
            "zipcode": random.randint(10000, 99999)
        }
    }

    people.append(d)

print people

# Example: 
# '{ "a": 12.5, "x": false }' # this is a string with json's format

# Serialize <people> data into a json's string
import json

# Code to json
people_json = json.dumps(people)

print type(people_json)

f = open("people.json", "w")

f.write(people_json)

f.close()