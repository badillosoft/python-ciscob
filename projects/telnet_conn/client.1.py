# _*_ coding: utf-8 _*_

from telnetlib import Telnet
import getpass

HOST = "localhost"
user = raw_input("User: ")
password = getpass.getpass()

tn = Telnet(HOST)

# Insert user
tn.read_until("login: ")
tn.write(user + "\n")

# Insert password
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls")
tn.write("exit")

print tn.read_all()