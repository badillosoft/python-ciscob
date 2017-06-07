from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "qty": { "$gte": 75 } } # qty>=75

for doc in db.inventory.find(query):
    print doc