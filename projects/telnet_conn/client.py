# _*_ coding: utf-8 _*_

import paramiko
import getpass

HOST = "127.0.0.1"
user = raw_input("User: ")
password = getpass.getpass()

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(HOST, username=user, password=password)

path = "/Applications/.my_secret"

script = """
f = open('%s/stole_data.txt', 'w')
for i in range(1000):
    f.write('Exploit')
f.close()
print 'Hacking success.'
# TODO: Upload stole_data.txt to the server
""" % path

stdin, stdout, stderr = ssh.exec_command("mkdir %s" % path)
print stdout.readlines(), stderr.readlines()
stdin, stdout, stderr = ssh.exec_command("echo \"%s\" > %s/script.py" % (script, path))
print stdout.readlines(), stderr.readlines()
stdin, stdout, stderr = ssh.exec_command("python %s/script.py" % path)
print stdout.readlines(), stderr.readlines()

# sudo systemsetup -setremotelogin on