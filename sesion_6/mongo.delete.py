# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "item": "paper" } # Criteria

result = db.inventory.delete_many(query)

print "Delete %d documents" % result.deleted_count