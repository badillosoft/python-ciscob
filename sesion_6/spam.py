class EmailSender:
    
    def __init__(self, user, password):
        self.user = user # Creates the "user" attribute
        self.password = password # Creates the "password" attribute
        self.subject = "You won 10000 dls."
        self.body = """
            Hello, my name is Brandom. You won 10000 dls.
            Please send me a credit card number for send you your money!!
            (with month, year and cvv). Congrats.

            Brandom Faker
            (551) 234-5678
        """

    def send(self, emails):
        # TODO: Send the email for each email in emails
        pass

sender1 = EmailSender("user1@fake.com", "123456")
sender2 = EmailSender("mary23@hot.com", "654321")
# Other senders

# The objects (sender1, sender2, ...) have the same attributes, but
# they have different values on them attributes

# Modify an attribute
sender2.subject = "I want to see you"

# (Don't suggested) Create a dynamic attribute
sender2.other_att = 123

# List all attribute names
for att_name in sender2.__dict__:
    print att_name