from Handler import Handler
from entities import Post


class ShowPostHandler(Handler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))

        if not post:
            self.error(404)
            return

        self.render('post.html', post=post)
