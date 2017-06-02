import util

emails = util.get_emails("contacts.txt")

user, password = util.get_user_pass()

util.program_send_emails(user, password, emails, "GG")