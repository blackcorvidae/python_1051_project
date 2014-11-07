import urllib
from pymongo import MongoClient
from bs4 import BeautifulSoup

def getUrl(base_url):
    # We want to use parameters eventually
    # params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    raw = urllib.urlopen(base_url)
    return raw


url = 'http://www.crummy.com/software/BeautifulSoup/'
html_object =  getUrl(url)
html_doc = html_object.read()

soup = BeautifulSoup(html_doc)
#print soup


print soup.title.name
print soup.title.string

findthis = "crummy"

try:
    for link in soup.find_all('a'):
        if link.get('href') is not None:
            if link.get('href').find(findthis) > 0: 
                print "Found Crummy"
                print(link.get('href'))
            else:
                print "Not Crummy"
                print(link.get('href'))
except:
   print "All is lost, abandon ship"
