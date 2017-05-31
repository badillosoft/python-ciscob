# _*_ coding: utf-8 _*_

f = open("my_file.txt", "r")

for line in f:
    print line[::-1]

f.close()