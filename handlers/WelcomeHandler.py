from Handler import Handler


class WelcomeHandler(Handler):
    def get(self):
        if self.user:
            self.render('index.html', username=self.user.username)
        else:
            self.redirect('/signup')
