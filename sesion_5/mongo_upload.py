# _*_ coding: utf-8 _*_

db_name = raw_input("DB: ")
coll_name = raw_input("Collection: ")
filename = raw_input("Filename: ")

from pymongo import MongoClient
import json

client = MongoClient()

db = client[db_name] # client.cisco or client["cisco"]

coll = db[coll_name] # db.my_coll or db["my_coll"]

f = open(filename, "r")

content = f.read() # JSON Formatted

f.close()

doc = json.loads(content)

coll.insert_one(doc)