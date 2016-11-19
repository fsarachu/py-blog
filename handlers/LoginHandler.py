from Handler import Handler
from entities import User
from helpers import PasswordHelper


class LoginHandler(Handler):
    def get(self):
        self.render('login.html')

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')

        params = dict(username=username)

        user = User.by_name(username)

        if not user or not PasswordHelper.check_password_hash(password, user.password):
            have_error = True
            params['error_login'] = 'Invalid login information'

        if have_error:
            self.render('login.html', **params)
        else:
            self.login(user)
            self.redirect('/')
