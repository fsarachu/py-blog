from Handler import Handler


class SignupHandler(Handler):
    def get(self):
        self.render('signup.html')
