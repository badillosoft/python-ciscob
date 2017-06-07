from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "size.w": { "$lt": 20 } } # size["w"] < 20

for doc in db.inventory.find(query):
    print doc