import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler)
], debug=True)
