import hashlib
import requests

def check_password_breach(password):
    """
    Checks if the password has been found in known data breaches using HaveIBeenPwned API.
    Returns the number of times it was found, or -1 if error.
    """
    try:
        sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            hashes = response.text
            for line in hashes.splitlines():
                hash_suffix, count = line.split(':')
                if hash_suffix == suffix:
                    return int(count)
            return 0
        else:
            return -1
    except Exception as e:
        return -1