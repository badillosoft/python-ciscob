from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "qty": { "$gte": 45, "$lt": 60 } } # qty >= 45 and qty < 60

for doc in db.inventory.find(query):
    print doc