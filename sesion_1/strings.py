# _*_ coding: utf-8 _*_

# How indexes works?

a = "hello world, this is python and works!"

print a[4]
print a[13:27] # get substring from 13 to 26 (include)
print a[:11] # start index is optional
print a[32:] # end index is optional too
print a[:] # Creates a copy with all elements (util in lists)

# Stepped index
print a[::2] # from 0 to n with two-step
print a[1::2] # from 1 to n with two-step

# Inverted
print a[::-1] # from n-1 to 0 with 1 negative step
print a[::-2] # from n-1 to 0 with 1 negative step