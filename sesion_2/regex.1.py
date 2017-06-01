# _*_ coding: utf-8 _*_

import re

text = "Av. Juarez #123, Doctores, Ciudad de Mexico."

pattern = "([\w\s.]+)#(\d+)[,.]\s*([\w\s.]+)[,.]\s*([\w\s.]+)"

for match in re.finditer(pattern, text):
    print match.group(0)
    print match.group(1)
    print match.group(2)
    print match.group(3)
    print match.group(4)

for match in re.findall(pattern, text):
    print match