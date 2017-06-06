# _*_ coding: utf-8 _*_

from pymongo import MongoClient
import re
import os

client = MongoClient()
db = client.oxxcisco
products = db.products

def insert_product(product):
    try:
        products.insert_one(product)
    except:
        print "Can't insert product"

# Product:
# name
# brand
# price:
#   unitary
#   constumer
# sizes
# weight
# bar_code
def print_product(product):
    print "-" * 39
    print "Name: %-20s (%10s)" % (product["name"], product["brand"])
    print "$%4.2f                  | %11s |" % (product["price"]["customer"], product["bar_code"])
    print "-" * 39
    print

def show_products():
    for prod in products.find():
        print_product(prod)

def home_menu():
    # print "\x1bc"
    os.system("clear") # "cls" on windows
    print "Welcome to OxxCisco v1.0"
    print
    print "Select an option:"
    print "1. Insert new product"
    print "2. Show all products"
    print "-" * 39
    print "x. Exit"
    print

    opt = raw_input("> ")

    if opt == "1":
        insert_menu()
    elif opt == "2":
        print "\x1bc"
        show_products()
        raw_input("press any key for continue...")
    elif re.match("^(x|q|quit|exit)$", opt, re.IGNORECASE):
        print "Bye!"
        return
    else:
        print "! The option is not valid"
        raw_input("press any key for continue...")

    home_menu() # Recursivity