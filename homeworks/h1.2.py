# _*_ coding: utf-8 _*_

a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
cuts = [2, 7, 9]

# Make a empty list, then put sublists here
splits = []

cc = 0 # current cut index

# First sublist is
ic = cc # fix
cc = cuts[0] # change (0)

s0 = a[ic:cc]  # fix (don't matter variable name)
splits.append(s0) # fix

# Second sublist is
ic = cc  # fix
cc = cuts[1] # change (1)

s1 = a[ic:cc] # fix
splits.append(s1) # fix

# Third sublist is (final)
ic = cc # fix
cc = cuts[2] # change (2) # How is the last index?

s2 = a[ic:cc] # fix
splits.append(s2) # fix

# How we can automate this process?

############################################################
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
cuts = [2, 7, 9]

splits = []

cc = 0 # current cut index

# The change is 0, 1, 2, ..., len(cuts)
for i in range(0, len(cuts)):
    ic = cc # fix
    cc = cuts[i] + 1 # change (i)
    s = a[ic:cc] # fix
    splits.append(s) # fix

ic = cuts[-1] + 1
s = a[ic:]
splits.append(s)

print splits