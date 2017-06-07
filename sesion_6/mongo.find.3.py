from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "$or": [
    { "item": "journal" }, # Q1
    { "item": "notebook" } # Q2
] } # Q1 or Q2

for doc in db.inventory.find(query):
    print doc