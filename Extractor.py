import urllib
from pymongo import MongoClient
from bs4 import BeautifulSoup

class Extractor:
    def __init__(self,base_url):
        self.base_url = base_url
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



                
