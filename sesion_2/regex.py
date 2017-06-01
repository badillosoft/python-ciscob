f = open("datos.txt", "r")

content = f.read()

f.close()

import re

# matches = re.findall(pattern, content)

pattern = "\(?\d{3}\)?([-\s]?\d){7}"

prog = re.compile(pattern)

# matches = prog.findall(content) # return a list of strings with the matches
iterator = prog.finditer(content)

for m in iterator:
    s, e = m.span()
    print content[s:e]
