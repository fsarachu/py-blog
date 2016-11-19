from Handler import Handler
from entities import Post


class MainHandler(Handler):
    def get(self):
        if self.user:
            posts = Post.all().order('-created').fetch(limit=10)
            self.render('index.html', user=self.user, posts=posts)
        else:
            self.redirect('/signup')
