# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

query = { "item": "notebook", "status": "C" } # Criteria
replace = { "$set": { "status": "X" } } # Update parts

# update_one only update one document matched by criteria
result = db.inventory.update_many(query, replace) 

print "Updated %d documents" % result.matched_count
