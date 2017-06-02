import smtplib
import getpass
import re

def login(email, password):
    smtpObj = smtplib.SMTP("smtp-mail.outlook.com", 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email, password)
    return smtpObj

def logout(smtpObj):
    smtpObj.quit()

def send_email(smtpObj, from_email, to_email, body):
    smtpObj.sendmail(from_email, to_email, body)
    print "Email was sent from %s to %s" %(from_email, to_email)

email = raw_input("Give your email: ")
password = getpass.getpass("Give your password: ")
message = raw_input("Write the message: ")

smtpObj = login(email, password)

# We are logged :D

# TO-DO: Get the emails from "contact.txt"
# 1. Get the content of "contacts.txt"
f = open("contacts.txt", "r")
content = f.read()
f.close()
# 2. Get the emails by pattern: [\w\.\-]+@\w{3,}\.(\w{2,})+
pattern = "[\w\.\-]+@\w{3,}\.(\w{2,})+"
# 3. For each email found send email
for m in re.finditer(pattern, content):
    to_email = m.group(0)
    send_email(smtpObj, email, to_email, "Subject: Hello from Python\n%s" % message)

logout(smtpObj)