import hmac
import random


class CookieHelper:
    def __init__(self):
        pass

    @staticmethod
    def hash_str(secret_key, message):
        return hmac.new(str(secret_key), str(message)).hexdigest()

    @staticmethod
    def make_secure_value(s, salt=None):
        if not salt:
            salt = CookieHelper.make_salt()
        return '{}-{}{}'.format(s, salt, CookieHelper.hash_str(salt, s))

    @staticmethod
    def check_secure_value(cookie_str):
        value = cookie_str.split('-')[0]
        salt = (cookie_str.split('-')[1])[:5]
        return value if cookie_str == CookieHelper.make_secure_value(value, salt) else None

    @staticmethod
    def make_salt(length=5):
        return ''.join(random.choice('1234567890abcdef') for _ in range(length))
