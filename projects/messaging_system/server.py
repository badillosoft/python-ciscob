# _*_ coding: utf-8 _*_

import json
from flask import Flask
from flask import request

app = Flask(__name__)

# Each username is unique, so it be the "key"
users = {
    "badillosoft": {
        "password": "123",
        "email": "badillo.soft@hotmail.com",
        "token": "ABCDEFG123456",
        "last": "2017-06-08T09:00:00Z06" # ISO-Datetime format
    }
}

@app.route("/")
def home():
    return "Hello"

@app.route("/login") # Default GET method
def login():
    user = request.args.get("user")
    password = request.args.get("password")
    
    result = {
        "error": True,
        "message": "Any message",
        "token": None
    }

    if users.has_key(user):
        # User exists
        if users[user]["password"] == password:
            # Credentials are valid
            result["error"] = False
            result["message"] = "User has been logged"
            result["token"] = users[user]["token"]
        else:
            result["message"] = "The password is incorrect"
    else:
        result["message"] = "User doesn't exist"

    return json.dumps(result)

# C:\Python27/Scripts/pip install flask

app.run() # run(host="10.10.3.225", port=3000)