from Handler import Handler


class MainHandler(Handler):
    def get(self):
        self.render('index.html')
