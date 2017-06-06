# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

it = db.test.find() # Return a cursor with the query

for doc in it:
    print "A: %d, B: %s, C: %s" % (doc["a"], doc["b"], doc["c"])