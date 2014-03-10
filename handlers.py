import webapp2
import urllib
from web import JINJA_ENVIRONMENT
import xml.etree.ElementTree as ET
from models import News


class Home(webapp2.RequestHandler):
  def get(self):
    news_query = News.query().order(-News.date)
    feeds = news_query.fetch(15)
    template = JINJA_ENVIRONMENT.get_template('templates/home.html')
    self.response.write(template.render({'feeds':feeds}))


class About(webapp2.RequestHandler):
  def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/about.html')
		self.response.write(template.render({'template_values':'ss'}))


class Contact(webapp2.RequestHandler):
  def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
		self.response.write(template.render({'template_values':'ss'}))


class Feed(webapp2.RequestHandler):
  def get(self):
    rss_feed = urllib.urlopen("https://news.ycombinator.com/rss")
    feeds = []
    try:
      tree = ET.parse(rss_feed)
      root = tree.getroot()
      items = root.find('channel').findall('item')
      for e in items:
        feeds.append({'title': e.find('title').text,
                     'link': e.find('link').text})
    except Exception, inst:
      print "Unexpected error opening %s: %s" % (tree, inst)

    for feed in feeds:
      news = News()
      setattr(news, 'title', feed['title'])
      setattr(news, 'link', feed['link'])
      news.put()