from HashHelper import HashHelper


class CookieHelper:
    def __init__(self):
        pass

    @staticmethod
    def make_secure_value(s, salt=None):
        if not salt:
            salt = HashHelper.make_salt()
        return '{}-{}{}'.format(s, salt, HashHelper.hash_str(salt, s))

    @staticmethod
    def check_secure_value(cookie_str):
        value = cookie_str.split('-')[0]
        salt = (cookie_str.split('-')[1])[:5]
        return value if cookie_str == CookieHelper.make_secure_value(value, salt) else None
