import webapp2

from handlers import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup', SignupHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/newpost', NewPostHandler),
    ('/(\d+)', ShowPostHandler),
    ('/user/(.*)', ShowUserHandler)
], debug=True)
