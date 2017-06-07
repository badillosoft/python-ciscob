# _*_ coding: utf-8 _*_

from pymongo import MongoClient
import os

client = MongoClient()
db = client.cisco

def add_contact():
    os.system("clear")
    print "Contact information"
    print "-" * 40
    print
    # What do you do in add_contact option? Request for contact data
    # What I want to storage? Name, Email, Phone numbers, etc.
    name = raw_input("Name: ")
    email = raw_input("Email: ")
    # How can I request several phone numbers?
    phones = []
    while True:
        phone = raw_input("Phone number: ")
        phones.append(phone)
        # TODO: Validate the phone number
        # TODO: Extract the phoner number into a standard format
        #   5512345678 => (551) 234-5678
        answ = raw_input("Do you want to add another phoner number? [Y/n] ")
        if answ == "n": # Better use regex for more complex options
            break # Manually breaks infinite loop
    # More data

    # What's next step? Create a dictionary for storage into a mongo's document
    contact = {
        "name": name,
        "email": email,
        "phones": phones
    }

    # Store the contact into mongo
    result = db.contacts.insert_one(contact)
    print
    print "Contact has been created with id:", result.inserted_id

def menu():
    os.system("clear")
    print "Select an option:"
    print
    print "1. Add contact"
    print "2. Find contact"
    print "3. Update contact"
    print "4. Delete contact"
    print "-" * 40
    print "x. Exit"
    print

    opt = raw_input("> ")

    if opt == "1":
        add_contact() # Delegate functionality to add_contact()
    elif opt == "2":
        find_contact() # Ask for search type: by name, by email, etc.
    elif opt == "3":
        update_contact() # Find the contact and update all fields
    elif opt == "4":
        delete_contact() # Find the contact and delete it
    elif opt == "x":
        print "Bye!"
        return
    else:
        print "Invalid option"
    
    raw_input("press any key to continue...")
    menu()

menu()