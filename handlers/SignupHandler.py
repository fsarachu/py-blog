from Handler import Handler
from entities import User
from validators import *


class SignupHandler(Handler):
    def get(self):
        self.render('signup.html')

    def post(self):
        have_error = False
        username = self.request.get('username')
        email = self.request.get('email')
        password = self.request.get('password')
        verify = self.request.get('verify')

        params = dict(username=username, email=email)

        if not SignupValidator.valid_username(username):
            params['error_username'] = 'Username is not valid!'
            have_error = True
        else:
            existing_user = User.all().filter('username =', username).get()
            if existing_user:
                params['error_username'] = 'Username already exists!'
                have_error = True

        if email != '' and not SignupValidator.valid_email(email):
            params['error_email'] = 'Email is not valid!'
            have_error = True

        if not SignupValidator.valid_password(password):
            params['error_password'] = 'Password is not valid!'
            have_error = True
        elif password != verify:
            params['error_verify'] = 'Passwords do not match!'
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            user = User.register(username, password, email)
            user.put()

            self.login(user)
            self.redirect('/')
