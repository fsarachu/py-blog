import jinja2
import os

import webapp2


class Handler(webapp2.RequestHandler):
    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')
    JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR), autoescape=True)

    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)

    def render(self, template_name, **kwargs):
        template = self.JINJA_ENV.get_template(template_name)
        self.write(template.render(kwargs))
