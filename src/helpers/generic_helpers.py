import random
import string


def generate_random_email(domain=None, email_prefix=None):
    if not domain:
        domain = "supersqa.com"

    if not email_prefix:
        email_prefix = "testuser"

    random_email_string_length = 10
    random_string = "".join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + "" + random_string + "@" + domain

    random_info = {"email": email}
    return random_info
