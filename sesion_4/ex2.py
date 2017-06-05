# _*_ coding: utf-8 _*_
# Generate a json's file with 2000 entries.
# Each entry describes one product, structured by:

# Product:
# name - The name [fake names]
# brand - The brand [fake brands]
# price - A dictionary with <u_price> and <c_price>
    # u_price - The unitary price [0.5, 200] random.uniform(a, b)
    # c_price - The costumer price [0.5, 200]
# bar_code - The bar-code [fake brands] 
#           Ex. ["0101002020", "2312312300", "231231230"] or [1000000000, 999999999999]
# quantity - The amount of existing products [0, 100]
# sizes - The minimum size h-w-d [1, 10]x[1, 10]x[1, 10] Ex. [3, 5, 6] (randint)
# weight - The weight [0.5, 20]

# 1. Generate a list of dictionaries (2000 random products)
# 2. Convert the list into a json's string
# 3. Save the string into "products.josn" file

# This function completes a number with zeros "0" if the string is less than n
def fillz(number, n):
    s = "%d" % number
    while len(s) < n:
        s = "0" + s
    return s

print fillz(10, 12)
print fillz(823, 6)

import random

start_names = ["Abc", "Def", "Ghi", "Jkl", "Mno", "Opq", "Rst"]
middle_names = ["cba", "fed", "ihg", "lkj", "onm", "tsr"]

products = []

for i in range(2000):
    s0 = random.choice(start_names) # C
    s1 = random.choice(start_names) # C
    s2 = random.choice(middle_names)
    s3 = random.choice(middle_names)
    s4 = random.choice(middle_names)
    s = "%s%s %s%s%s" % (s0, s2, s1, s3, s4)

    r0 = random.choice(start_names) # C
    r1 = random.choice(start_names) # C
    r2 = random.choice(middle_names)
    r3 = random.choice(middle_names)
    r4 = random.choice(middle_names)
    b = "%s%s%s %s%s" % (r0, r2, r3, r1, r4)
    
    up = random.uniform(0.5, 100)
    cp = up * random.uniform(1.1, 1.5)

    product = {
        "name": s,
        "brand": b,
        "price": {
            "unitary": up,
            "costumer": cp
        },
        "bar_code": fillz(random.randint(0, 99999999999), 11),
        "quantity": random.randint(0, 20),
        "sizes": [
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 10),
        ],
        "weight": random.uniform(0.5, 20)
    }

    products.append(product)

import json

data = json.dumps(products)

f = open("products.json", "w")

f.write(data)

f.close()
