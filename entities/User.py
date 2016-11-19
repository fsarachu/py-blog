from google.appengine.ext import db


class User(db.Model):
    username = db.StringProperty(required=True)
    email = db.EmailProperty()
    password = db.StringProperty(required=True)
