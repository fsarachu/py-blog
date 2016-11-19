from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    email = db.EmailProperty()
    password = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, user_id):
        return User.get_by_id(user_id)
