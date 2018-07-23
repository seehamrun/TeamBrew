import webapp2
import logging
import jinja2
import os
import json

from google.appengine.ext import ndb
from google.appengine.api import urlfetch


class WardrobeSave(ndb.Model):
    url = ndb.StringProperty()


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainPage(webapp2.RequestHandler):
    def get(self):
        response_html = jinja_env.get_template("templates/main_page.html")


#class AddItem(webapp2.RequestHandler):

class AddClothingHandler(webapp2.RequestHandler):
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> ede39b778a1ff8d9f7814f2ae512f0dcef6de985
>>>>>>> cab10dc06b57e9a4085230c3d2deb9f19059e1ff
    def get(self):
        response_html = jinja_env.get_template("Imgur-Upload-master/index.html")
        self.response.headers['Content-Type'] = 'text/html'
        return self.response.write(response_html.render())
<<<<<<< HEAD
=======

>>>>>>> cab10dc06b57e9a4085230c3d2deb9f19059e1ff
    def post(self):
        requestUrl = self.request.get('url')
        logging.info('server saw a request to add %s to list of favorites' % (requestUrl))
        favoriteUrl = AddClothing(url=requestUrl)
        favoriteUrl.put()


class WardrobePage(webapp2.RequestHandler):
    def get(self):
        response_html = jinja_env.get_template("templates/wardrobe_page.html")


app = webapp2.WSGIApplication([
<<<<<<< HEAD
    ('/', MainPage),
    ('/Wardrobe', WardrobePage),
    ('/add_favorite', AddClothingHandler)
=======
<<<<<<< HEAD
#    ('/add_favorite', AddClothingHandler),
=======
    ('/add_favorite', AddClothingHandler),
>>>>>>> ede39b778a1ff8d9f7814f2ae512f0dcef6de985
    ('/', MainPage),
    ('/Wardrobe', WardrobePage),
    ('/AddItem', AddItem),
    ('/Suggestions', Suggestions),
    ('/Outfits', Outfits),
    ('/add_favorite', AddFavoriteHandler),
>>>>>>> cab10dc06b57e9a4085230c3d2deb9f19059e1ff
], debug=True)
