import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler)
], debug=True)
