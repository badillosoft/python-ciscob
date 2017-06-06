# _*_ coding: utf-8 _*_

from pymongo import MongoClient

# Binds a client to MongoDB
client = MongoClient() # MongoClient(port=27018)

# Binds a Database called "cisco"
db = client.cisco # If db doesn't exists it will be created

coll = db.test # If collection doesn't exists it will be created

# Insert data
# Python's dictionaries are equivalent with mongo's documents
coll.insert_one({ "a": 13, "b": True, "c": "Hello" }) # Storage a document { ... }

# Mongo assign an implicit id called "_id" (key _id has a ObjectId value)
coll.insert_many([
    {
        "a": 15,
        "b": False,
        "c": "Hi"
    },
    {
        "a": 27,
        "b": None,
        "c": "GG"
    }
])