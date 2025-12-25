import random
import string

def generate_password(length=12):
    """
    Generates a strong password of given length.
    """
    if length < 8:
        length = 8

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*(),.?\":{}|<>"

    # Ensure at least one of each
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest
    all_chars = lowercase + uppercase + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle
    random.shuffle(password)
    return ''.join(password)