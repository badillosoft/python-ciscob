# We need to save a list of points

# Each point is (x, y)

points = [
    (3, 4),
    (6, 8),
    (9, 11),
    (6, 7)
]

print points[2]

x2, y2 = points[2]

print x2
print y2

for t in points:
    x, y = t
    r = (x ** 2 + y ** 2) ** 0.5
    print r

for x, y in points:
    r = (x ** 2 + y ** 2) ** 0.5
    print r