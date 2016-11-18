import hmac
import random
import string


class CookieHelper:
    def __init__(self):
        pass

    @staticmethod
    def hash_str(secret_key, message):
        return hmac.new(secret_key, message).hexdigest()

    @staticmethod
    def make_secure_value(s, salt=None):
        if not salt:
            salt = CookieHelper.make_salt()
        return '{}-{},{}'.format(s, salt, CookieHelper.hash_str(salt, s))

    @staticmethod
    def check_secure_value(s):
        value = s.split('-')[0]
        salt = (s.split('-')[1]).split(',')[0]
        return value if s == CookieHelper.make_secure_value(value, salt) else None

    @staticmethod
    def make_salt(length=5):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
