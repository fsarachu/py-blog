from Handler import Handler


class MainHandler(Handler):
    def get(self):
        if self.user:
            self.render('index.html', username=self.user.username)
        else:
            self.redirect('/login')
