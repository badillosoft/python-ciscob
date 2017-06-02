# _*_ coding: utf-8 _*_

import re

f = open("%s/ip_log.txt", "r")

ip_log = f.read()

f.close()

pattern = "(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"

fo = open("ip_clear.txt", "w")

for m in re.finditer(pattern, ip_log):
    n1 = int(m.group(1))
    n2 = int(m.group(2))
    n3 = int(m.group(3))
    n4 = int(m.group(4))

    if n1 > 255 or n2 > 255 or n3 > 255 or n4 > 255:
        continue # Continue with the next iteration

    fo.write("%d.%d.%d.%d\n" % (n1, n2, n3, n4))

fo.close()