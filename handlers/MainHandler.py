from Handler import Handler


class MainHandler(Handler):
    def get(self):
        self.render('index.html')
        # user_id = self.request.cookies.get('user_id')
        #
        # if user_id:
        #     # Get user from db and then..
        #     self.render('index.html')
        # else:
        #     self.redirect('/signup')
