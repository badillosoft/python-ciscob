# _*_ coding: utf-8 _*_

# Sort a list

def sort(a):
    b = []

    n = len(a)

    for i in range(n): # Repeat n-times
        x = min(a) # Find the min element
        b.append(x) # Save the min element in sorted list
        a.remove(x) # Removes the min element for unsorted list

    return b

print sort([
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
    1, 2, 3, 5, 2, 3, 5, 3, 7, 8, 
])
