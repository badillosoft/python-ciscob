# _*_ coding: utf-8 _*_

# We need to save points in a list with dictionary structure

points = [
    {
        "x": 1,
        "y": 5
    },
    {
        "x": 6,
        "y": 9
    }
]

# Generate 100 points with the next rules:
# x = i
# y = i ** 2

for i in range(1, 101):
    d = {}

    d["x"] = i
    d["y"] = i ** 2

    points.append(d)

print points