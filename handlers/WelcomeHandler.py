from Handler import Handler
from helpers import CookieHelper


class WelcomeHandler(Handler):
    def get(self):
        username_cookie_str = self.request.cookies.get('username')
        if not username_cookie_str:
            self.redirect('/signup')
        else:
            username = CookieHelper.check_secure_value(username_cookie_str)
            if not username:
                self.redirect('/signup')
            else:
                self.render('index.html', username=username)
