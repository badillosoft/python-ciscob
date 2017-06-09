# _*_ coding: utf-8 _*_

import paramiko
import getpass

HOST = "127.0.0.1"
user = raw_input("User: ")
password = getpass.getpass()

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(HOST, username=user, password=password)

stdin, stdout, stderr = ssh.exec_command("cd /Applications")
stdin, stdout, stderr = ssh.exec_command("mkdir my_secret")
stdin, stdout, stderr = ssh.exec_command("cd my_secret")
stdin, stdout, stderr = ssh.exec_command("echo 'print \"Hack\"' > script.py")
stdin, stdout, stderr = ssh.exec_command("python script.py")

print stdout.readlines()

# sudo systemsetup -setremotelogin on