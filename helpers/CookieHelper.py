from HashHelper import HashHelper


class CookieHelper:
    SECRET = 'I$U{=GbJj![J~fi"#.te'

    def __init__(self):
        pass

    @staticmethod
    def make_secure_value(s):
        return '{}-{}'.format(s, HashHelper.hash_str(CookieHelper.SECRET, s))

    @staticmethod
    def check_secure_value(cookie_str):
        value = cookie_str.split('-')[0]
        if cookie_str == CookieHelper.make_secure_value(value):
            return value

    @staticmethod
    def set_secure_cookie(handler, name, value):
        handler.response.headers.add_header(
            'Set-cookie',
            '{}={}; Path=/'.format(name, value)
        )

