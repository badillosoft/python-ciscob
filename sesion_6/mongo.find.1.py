from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "item": "journal" } # item=journal

for doc in db.inventory.find(query):
    print doc