# _*_ coding: utf-8 _*_
import os
import urllib
import urllib2
import json

BASE_URL = "http://localhost:5000"

username = ""
token = ""

def login():
    global token, username

    os.system("clear")
    username = raw_input("User: ")
    password = raw_input("Password: ")

    response = urllib2.urlopen("%s/login?user=%s&password=%s" % (BASE_URL, username, password))
    content = response.read()
    result = json.loads(content)

    if result["error"]:
        print result["message"]
        return

    print result["message"]
    token = result["token"]

def send():
    os.system("clear")
    message = raw_input("Enter a message: ")

    message = urllib.pathname2url(message)

    url = "%s/%s/send?m=%s&token=%s" % (BASE_URL, username, message, token)

    response = urllib2.urlopen(url)
    content = response.read()

    result = json.loads(content)

    print result["message"]

def menu():
    os.system("clear")

    if username != "" and token != "":
        print "Welcome %s" % username
        print

    print "Select an option:"
    print
    print "1. Login to system"
    print "2. Send a message"
    print "3. View new messages"
    print "-" * 50
    print "x. Exit"
    print

    opt = raw_input("> ")

    if opt == "1":
        login()
    elif opt == "2":
        send()
    elif opt == "3":
        messages()
    elif opt == "x":
        print "Bye!"
        return
    else:
        print "Invalid option"

    raw_input("press any key to continue...")
    menu()

menu()