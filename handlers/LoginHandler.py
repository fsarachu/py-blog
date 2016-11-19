from Handler import Handler
from helpers import CookieHelper


class LoginHandler(Handler):
    def get(self):
        self.render('login.html')

    def do_login(self, user):
        CookieHelper.set_secure_cookie(self, 'user_id', user.key().id())
