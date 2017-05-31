# _*_ coding: utf-8 _*_

# Dictionaries

# Is a pair data (key-value) in a set

person = {
    "name": "Pepe",
    "old": 32,
    "email": "pepe@hotmail.com",
    "address": {
        "street": "Av. Boulevard",
        "zip_code": "12345"
    }
}

print person["name"]
print person["email"]
print person["address"]["street"]

if person.has_key("last"):
    print person["last"]
else:
    person["last"] = "Undefined"

print person