# _*_ coding: utf-8 _*_

import re

f = open("ip_log.txt", "r")

ip_log = f.read()

f.close()

pattern = "(\d{1,3}\.){3}\d{1,3}"

fo = open("ip_clear.txt", "w")

for m in re.finditer(pattern, ip_log):
    ip = m.group(0)
    fo.write("%s\n" % ip)

fo.close()