from Handler import Handler


class MainHandler(Handler):
    def get(self):
        username = self.request.cookies.get('username')

        if username:
            self.render('index.html', username=username)
        else:
            self.redirect('/signup')
