from Handler import Handler
from entities import Post


class NewPostHandler(Handler):
    def get(self):
        if not self.user:
            self.redirect('/login')
        else:
            self.render('new_post.html')

    def post(self):
        if not self.user:
            self.redirect('/login')
            return

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            new_post = Post(author=self.user, subject=subject, content=content)
            new_post.put()
            self.redirect('/' + str(new_post.key().id()))
        else:
            error = 'You must provide both subject and content.'
            self.render('new_post.html', subject=subject, content=content, error=error)
