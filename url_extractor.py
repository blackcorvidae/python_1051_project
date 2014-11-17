import urllib
import sys, getopt
from pymongo import MongoClient
from bs4 import BeautifulSoup
from Extractor import *

def main(argv):
   

   inputfile = ''
   outputfile = ''
   
   url = 'http://www.crummy.com/software/BeautifulSoup/'
   findthis = "www.crummy.com"
   
   do_config = False
   get_config = False
   do_get_url = False

   try:
      opts, args = getopt.getopt(argv,"hrcgi:o:u:k:",["ifile=","ofile=","ufile=","kfile="])
   except getopt.GetoptError:
      print 'url_extractor.py -h'
      print 'url_extractor.py -i <inputfile> -o <outputfile>'
      print 'url_extractor.py -u <base_url> -k <keyword>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'url_extractor.py -h'
         print 'url_extractor.py -i <inputfile> -o <outputfile>'
         print 'url_extractor.py -u <base_url> -k <keyword>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt == '-c':
         do_config = True
      elif opt == '-g':
         get_config = True
      elif opt == '-r':
         do_get_url = True
      elif opt in ("-u", "--ufile"):
         url = arg
      elif opt in ("-k", "--kfile"):
         findthis = arg

   extract = Extractor(url)

   if do_config:
       #Config
       post = {"base_url": url, "keyword": findthis, "updated": datetime.datetime.utcnow()}
       extract.add_config(post)

   if get_config:
       criteria = {}
       config = extract.get_config(criteria)
       print config
       print config["_id"]
       print config["base_url"]

   if do_get_url:
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

   
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   print 'Base url is "', url
   print 'Keyword is "', findthis
   

if __name__ == "__main__":
   main(sys.argv[1:])










