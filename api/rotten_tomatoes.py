__author__ = 'gabriel'
import json
import requests
import settings


class RottenTomatoes(object):
    def __init__(self):
        self.root_url = 'http://api.rottentomatoes.com/api/public/v1.0.json'
        self.connect()

    def connect(self):
        self.conn = r = requests.get(self.root_url, params={'apikey': settings.ROTTENTOM_API_KEY})
        if not r.ok:
            raise requests.ConnectionError()

    def search_movie(self, title):
        pass