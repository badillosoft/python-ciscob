# _*_ coding: utf-8 _*_

# Tuples

# A list inmutable (don't change)

t = (1, 3, 5)

# t[0] = 2 # ERROR
# t.append(7) # ERROR
# t.pop() # ERROR

# To package elements

# Packge / Unpackage

# Unpackage: Assign a variable to each element of tuple

a, b, c = t

print a
print b
print c

x = [1, 2, 3]
y = [4, 7, 9]

t = (x, y)

# ...

print t

x.append(4)

print t

X, Y = t
