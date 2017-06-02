# _*_ coding: utf-8 _*_

s = "a = 123 + 246 * {124 + 16 * 2} + {24 * 38 - 12} / {54 - 29 + 1}"

import re

for m in re.finditer("\{([\w\s\+\*\-]*)\}", s): # ..(P)..
    print m.group(1)

 # Pattern: "(P)..(Q)..(R)"
 # G0: (P)..(Q)..(R)
 # G1: P
 # G2: Q
 # G3: R