# _*_ coding: utf-8 _*_

s = "a = 123 + 246 * (124 + 16 * 2)"

# Problem: Get content inside (·) Ex. 124 + 16

si = -1 # Start index of (
ei = -1 # End index of )

for i in range(len(s)):
    if s[i] == "(":
        si = i
    if s[i] == ")":
        ei = i

sub = s[(si+1):ei]

print sub

# Second form
si = -1
ei = -1

for c in s:
    if c == "(":
        si = s.index(c)
    if c == ")":
        ei = s.index(c)

si = s.index("(")
ei = s.index(")")

sub = s[(si+1):ei]

print sub