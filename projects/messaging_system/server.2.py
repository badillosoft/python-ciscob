# _*_ coding: utf-8 _*_

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
    print user, password
    return "User: %s Password: %s" % (user, password)

# C:\Python27/Scripts/pip install flask

app.run() # run(host="10.10.3.225", port=3000)