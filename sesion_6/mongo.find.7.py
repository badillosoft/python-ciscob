# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

# starts with foo: ^foo
# contains foo: foo
# ends with foo: foo$
query = { "item": { "$regex": "PAPER", "$options": "i" } } # re.match(pattern, item)

for doc in db.inventory.find(query):
    print doc