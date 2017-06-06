from pymongo import MongoClient

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
    print "Name: %20s (%10s)" % (product["name"], product["brand"])
    print "$%4.2f                 | %11s |" % (product["price"]["costumer"], product["bar_code"])
    print "-" * 39

def show_products():
    for prod in products.find():
        print_product(prod)