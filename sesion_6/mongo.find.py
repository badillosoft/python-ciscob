from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = {} # Query is the search-restrictions

for doc in db.inventory.find(query):
    print doc