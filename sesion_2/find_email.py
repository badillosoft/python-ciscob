# _*_ coding: utf-8 _*_

# Find all emails in the file "datos.txt"

# Cannoical mode
# matches = re.findall(pattern, text)

# Optimized mode
# prog = re.compile(pattern)
# matches = prog.findall(pattern)

# Find all matches (non-overlapping)
# findall(text)

# Find all one-by-one
# finditer(text)

# Best simple-way
# for match in re.finditer(pattern, text):
#   print match.group(0)

import re

f = open("datos.txt", "r")

text = f.read()

f.close()

pattern = "[\w\.-]+@[\w]{3,}\.([\w\.]{2,})+"

for match in re.finditer(pattern, text):
    print match.group(0)