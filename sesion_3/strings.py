s = "a = 123 + 246"

# First task: Get the "=" index
# for i in s: # What iter? index or element? A: By element
# for i in range(len(s)): # A: By index

eqi = -1 # Initialize in invalid index

# The -1 is an invalid index, only agree by us
# By convention

for i in range(len(s)):
    if s[i] == "=":
        eqi = i

if eqi < 0:
    print "= not found"

# Second form
eqi = -1

#for c in s:
#    if c == "=":
#        eqi = s.index(c)

eqi = s.index("=") # To memorize or google hints