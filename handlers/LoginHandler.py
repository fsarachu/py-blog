from Handler import Handler
from helpers import CookieHelper


class LoginHandler(Handler):
    def get(self):
        self.render('login.html')

