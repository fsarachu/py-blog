import hashlib
import hmac
import random


class HashHelper:
    def __init__(self):
        pass

    @staticmethod
    def hash_str(secret_key, message):
        return hmac.new(str(secret_key), str(message), hashlib.sha256).hexdigest()

    @staticmethod
    def make_salt(length=5):
        return ''.join(random.choice('1234567890abcdef') for _ in range(length))
