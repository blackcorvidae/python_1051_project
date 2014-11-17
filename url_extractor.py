import urllib
from pymongo import MongoClient
from bs4 import BeautifulSoup
from Extractor import *

url = 'http://www.crummy.com/software/BeautifulSoup/'
extract = Extractor(url)


#Config
findthis = "www.crummy.com"
post = {"base_url": url, "keyword": findthis, "updated": datetime.datetime.utcnow()}
extract.add_config(post)




#Reading
html_object =  extract.get_html_from_url()
#html_object =  getUrl(url)
html_doc = html_object.read()
list_of_hrefs = extract.find_keyword_in_href(findthis, html_doc)


if list_of_hrefs:
    for href in list_of_hrefs:
        #print href
        extract.add_url_to_collected(href)

collected_urls = extract.get_collected_urls()
for url in collected_urls:
    print url


