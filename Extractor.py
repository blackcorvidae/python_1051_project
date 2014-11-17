import urllib
from pymongo import MongoClient
from bs4 import BeautifulSoup
import datetime

class Extractor:
    def __init__(self,base_url):
        self.base_url = base_url
    def add_config(self, post):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.dom_project
        collection = db.options
        post_id = collection.insert(post)
        return post_id
    def get_config(self, criteria):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.dom_project
        collection = db.options
        return collection.find_one()

    collected_urls = []
    def add_url_to_collected(self, url):
        if not self.search_collected_urls(url):
            self.collected_urls.append(url)
    def get_collected_urls(self):
        return self.collected_urls
    def search_collected_urls(self, find_url):
        for url in self.collected_urls:
            if url == find_url:
                return True
            else:
                return False
    def iterate_hrefs_by_keyword(self, keyword, html_doc):
        list_of_hrefs = self.find_keyword_in_href(keyword, html_doc)
        if list_of_hrefs:
            for href in list_of_hrefs:
                #print href
                self.add_url_to_collected(href)
    def get_html_from_url(self):
        # We want to use parameters eventually
        # params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
        raw = urllib.urlopen(self.base_url)
        return raw
    def find_keyword_in_href(self, findthis, html_doc):
        href_matches = []
        soup = BeautifulSoup(html_doc)
        #print soup
        #print soup.title.name
        #print soup.title.string
        #findthis = "crummy"
        try:
            for link in soup.find_all('a'):
                if link.get('href') is not None:
                    if link.get('href').find(findthis) > 0:
                        #print "Found Crummy"
                        href_matches.append(link.get('href'))
                    else:
                        #print "Not Crummy"
                        pass
        except:
            print "All is lost, abandon ship"
            href_matches = False
        return href_matches



                
