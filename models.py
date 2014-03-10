from google.appengine.ext import ndb


class News(ndb.Model):
    """Models an individual News entry with title, link, and date."""
    title = ndb.StringProperty(indexed=False)
    link = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)