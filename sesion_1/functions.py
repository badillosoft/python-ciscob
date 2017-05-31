# _*_ coding: utf-8 _*_

# Function: A block of code with params

# Generate n-integers
def gen(n):
    a = []
    
    for i in range(1, n + 1):
        a.append(i)
    
    return a

print gen(10)
print gen(5)
print gen(50)

# We can storage the return data in local variable b
b = gen(100)

print b[10]