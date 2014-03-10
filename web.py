import os
import urllib

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

application = webapp2.WSGIApplication([
  ('/', 'handlers.Home'),
  ('/reach', 'handlers.Contact'),
  ('/who', 'handlers.About'),
  ('/feed', 'handlers.Feed'),
  ('/login/', 'handlers.Login')
  ], debug=True)
