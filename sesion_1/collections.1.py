# We need to generate a list of numbers between [1, 100]
# save only the even numbers

a = []

for i in range(1, 101):
    if i % 2 == 0:
        # i is even
        a.append(i)