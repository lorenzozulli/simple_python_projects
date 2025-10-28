import string
import secrets

class Account(object):
    def __init__(self, identifier, title, username, email, password):
        self.identifier = identifier
        self.title = title
        self.username = username
        self.email = email
        self.password = password

    def password_generator(password_length):
        usable_characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(secrets.choice(usable_characters) for i in range(int(password_length)))

        while True:
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_symbol = any(c in string.punctuation for c in password)

            if has_upper and has_lower and has_digit and has_symbol:
                break
            else:
                password = ''.join(secrets.choice(usable_characters) for i in range(password_length))
        return password