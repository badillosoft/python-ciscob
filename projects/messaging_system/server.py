# _*_ coding: utf-8 _*_

import json
import datetime
from flask import Flask
from flask import request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.cisco

@app.route("/")
def home():
    return "Hello"

@app.route("/<username>/send")
def send(username):
    user = db.users.find_one({ "username": username })

    result = {
        "error": True,
        "message": "Any message"
    }

    if not user:
        result["message"] = "Invalid user"
        return json.dumps(result)

    message = request.args.get("m")
    token = request.args.get("token")

    if user["token"] != token:
        result["message"] = "Invalid token >:("
        return json.dumps(result)

    if request.args.get("to"):
        # TODO: Handle the process peer-to-peer message
        pass

    # TODO: Store the message and notify to other clients
    db.messages.insert_one({
        "user": username,
        "content": message,
        "seen": [username],
        "hearts": 0,
        "datetime": datetime.datetime.now().isoformat() # The current datetime
    })

    result["message"] = "Your message was sent"
    return json.dumps(result)

@app.route("/login") # Default GET method
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    
    if not user:
        user = ""
    
    if not password:
        password = ""

    result = {
        "error": True,
        "message": "Incorrect login",
        "token": None
    }

    print user, password

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