from google.appengine.ext import db

from helpers import PasswordHelper


class User(db.Model):
    username = db.StringProperty(required=True)
    email = db.StringProperty()
    password = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, user_id):
        return User.get_by_id(int(user_id))

    @classmethod
    def by_name(cls, username):
        user = User.all().filter('name =', username).get()
        return user

    @classmethod
    def register(cls, username, password, email=None):
        password_hash = PasswordHelper.make_password_hash(password)
        return User(username=username, password=password_hash, email=email)

    @classmethod
    def login(cls, username, password):
        user = cls.by_name(username)
        if user and PasswordHelper.check_password_hash(password, user.password):
            return user
