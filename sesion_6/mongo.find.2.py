from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "item": "journal", "status": "B" } # item=journal and status=B

for doc in db.inventory.find(query):
    print doc