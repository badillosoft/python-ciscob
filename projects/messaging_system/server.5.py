# _*_ coding: utf-8 _*_

import json
from flask import Flask
from flask import request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.cisco

@app.route("/")
def home():
    return "Hello"

@app.route("/login") # Default GET method
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    
    result = {
        "error": True,
        "message": "Incorrect login",
        "token": None
    }

    query = {
        "username": user,
        "password": password
    } # Criteria for search

    real_user = db.users.find_one(query)

    if real_user:
        result["error"] = False
        result["message"] = "User has been logged"
        result["token"] = real_user["token"]
    else:
        result["message"] = "The credentials do not match"

    return json.dumps(result)

# C:\Python27/Scripts/pip install flask

app.run() # run(host="10.10.3.225", port=3000)