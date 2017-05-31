# _*_ coding: utf-8 _*_

# Lists [,]
# Tuples (,)
# Dictionaries {,}

# Lists - Array of data

a = [1, 2, 3, 4] # Auto-asign indices starting 0

print a[2]

# Important methods

# Add elements
# append(x) -- Add the "x" element at end
# insert(i, x) -- Inserts "x" element at "i" index

# Remove elements
# pop(i) -- Remove "i" element and return it (optional i)
# remove(x) -- Remove the first "x" findend

# Size of list
# len(my_list) -- Get the current size of my_list

# a.pop(1)
# a.remove(2)

# a.append(5)
# a.insert(4, 5)

# Generate a list with the first 100 integers

b = []

# Iterator (for-in)
# Iterable (collection or range)
# Iterand (i, x, ...)
for i in range(1, 101):
    b.append(i)

print b