from Handler import Handler
from entities import User


class LoginHandler(Handler):
    def get(self):
        self.render('login.html')

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')

        params = dict(username=username)

        user = User.login(username, password)

        if not user:
            params['error_login'] = 'Invalid username or password!'
            self.render('login.html', **params)
        else:
            self.login(user)
            self.redirect('/')
