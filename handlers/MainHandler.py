from Handler import Handler


class MainHandler(Handler):
    def get(self):
        if self.user:
            self.render('index.html', user=self.user)
        else:
            self.redirect('/signup')
