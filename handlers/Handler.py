import jinja2
import os

import webapp2

from entities import User
from helpers import CookieHelper


class Handler(webapp2.RequestHandler):
    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')
    JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)

    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)

    def render(self, template_name, **kwargs):
        template = self.JINJA_ENV.get_template(template_name)
        self.write(template.render(kwargs))

    def set_secure_cookie(self, name, value):
        self.response.headers.add_header(
            'Set-cookie',
            '{}={}; Path=/'.format(name, CookieHelper.make_secure_value(value))
        )

    def read_secure_cookie(self, name):
        cookie_value = self.request.cookies.get(name)
        if cookie_value:
            return CookieHelper.check_secure_value(cookie_value)

    # noinspection PyAttributeOutsideInit
    def initialize(self, *args, **kwargs):
        webapp2.RequestHandler.initialize(self, *args, **kwargs)
        user_id = self.read_secure_cookie('user_id')
        if user_id:
            self.user = User.by_id(user_id)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
