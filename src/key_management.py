from os import urandom
import base64

def generate_key():
    return urandom(32)

def save_key(key, filename='key.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(base64.urlsafe_b64encode(key))

def load_key(filename='key.key'):
    with open(filename, 'rb') as key_file:
        key = base64.urlsafe_b64decode(key_file.read())
    return key
