# _*_ coding: utf-8 _*_

s = "a = 123 + 246 * (124 + 16 * 2) + (24 * 38 - 12) / (54 - 29 + 1)"

inside = False # Inside a parenthesis

sub = ""

for c in s:
    if c == "(":
        inside = True
    elif c == ")":
        print sub
        sub = "" # Reset
        inside = False
    elif inside: # Check if inside == True
        sub += c # sub = sub + c <concat>