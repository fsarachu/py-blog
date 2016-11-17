import re


class SignupValidator:
    def __init__(self):
        pass

    USER_RE = re.compile(r'^[a-zA-Z0-9_-]{3,20}$')
    PASS_RE = re.compile(r'^.{3,20}$')
    EMAIL_RE = re.compile(r'^[\S]+@[\S]+.[\S]+$')

    @staticmethod
    def valid_username(username):
        return SignupValidator.USER_RE.match(username)

    @staticmethod
    def valid_password(password):
        return SignupValidator.PASS_RE.match(password)

    @staticmethod
    def valid_email(email):
        return SignupValidator.EMAIL_RE.match(email)
