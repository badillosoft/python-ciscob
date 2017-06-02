# _*_ coding: utf-8 _*_

s = "a = 123 + 246 * (124 + 16 * 2) + (24 * 38 - 12) / (54 - 29 + 1)"

# We need a list ["124 + 16 * 2", "24 * 38 - 12", "54 - 29 + 1"]

# We need a loop

# Syntax: 
# while <condition>:
#   block

# Repeat the loop forever
i = 0 # Start the search from 0
while True:
    # To handle a possible exception we need to embed the code that raise an exception
    # try - except
    try:
        si = s.index("(", i)
        ei = s.index(")", i)
    except: # There is an exception
        print "They are not more (·)"
        break # Break the infinite loop (break the while)
    else: # There is not an exception
        sub = s[si+1:ei]
        print sub # TO-DO: Add the sub into a list
        i = ei + 1

    # Other code

# Continue here