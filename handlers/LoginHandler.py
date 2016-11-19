from Handler import Handler
from helpers import CookieHelper


class LoginHandler(Handler):
    def get(self):
        self.render('login.html')

    def do_login(self, user):
        self.response.headers.add_header('Set-Cookie',
                                         'username={}; Path=/'.format(
                                             CookieHelper.make_secure_value(user.key().id())))
