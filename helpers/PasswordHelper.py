from helpers import HashHelper


class PasswordHelper:
    @staticmethod
    def make_password_hash(plain_password, salt=None):
        if not salt:
            salt = HashHelper.make_salt()

        password_hash = '{}{}'.format(salt, HashHelper.hash_str(salt, plain_password))
        return password_hash

    @staticmethod
    def check_password_hash(plain_password, password_hash):
        salt = password_hash[:5]
        return password_hash == PasswordHelper.make_password_hash(plain_password, salt)
