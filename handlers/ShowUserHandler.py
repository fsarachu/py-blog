from Handler import Handler
from entities import User


class ShowUserHandler(Handler):
    def get(self, username):
        user = User.by_name(username)

        if not user:
            self.error(404)
            return

        self.render('user.html', user=user)
