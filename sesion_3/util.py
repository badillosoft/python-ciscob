import smtplib
import getpass
import re

def login(email, password):
    smtpObj = smtplib.SMTP("smtp-mail.outlook.com", 587)
    # GMAIL: smtp.gmail.com
    # HOTMAIL: smtp-mail.outlook.com
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(email, password)
    return smtpObj

def logout(smtpObj):
    smtpObj.quit()

def send_email(smtpObj, from_email, to_email, body):
    smtpObj.sendmail(from_email, to_email, body)
    print "Email was sent from %s to %s" %(from_email, to_email)

def program_send_emails(user, password, emails, message):
    so = login(user, password)
    print "Ready to send emails to:", emails
    for email in emails:
        send_email(so, user, email, message)
    logout(so)

def get_emails(source):
    pattern = "[\w\.\-]+@\w{3,}\.(\w{2,})+"
    f = open(source, "r")
    content = f.read()
    f.close()
    emails = []
    for m in re.finditer(pattern, content):
        email = m.group(0)
        emails.append(email)
    return emails

def get_user_pass():
    user = raw_input("User: ")
    password = getpass.getpass("Password: ")
    return (user, password)