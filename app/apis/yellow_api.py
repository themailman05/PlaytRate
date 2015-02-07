"""
API interface for YellowPages (Canada)

@author: David McVicar
"""


import urllib
import urllib2
import json
import time

HOST = 'http://api.sandbox.yellowapi.com'
API_KEY = '9xk456gspvxxqpr9nugmaumq'
UNIQUE_ID = 'mouthfeel'
FMT = 'JSON'

FIND_BUSINESS = '/FindBusiness/?'
GET_BUSINESS_DETAILS = '/GetBusinessDetails/?'

#Search parameters


def search(term, location):

   url = HOST +\
   FIND_BUSINESS +\
   "what=" + urllib.quote(term.encode('utf8')) +\
   "&where=" + urllib.quote(location.encode('utf8')) +\
   "&fmt=" + FMT +\
   "&apikey=" + API_KEY +\
   "&UID=" + UNIQUE_ID
   
   conn = urllib2.urlopen(url,None)
   try:
      response = json.loads(conn.read())
   finally:
      conn.close()

   return response

def get_business_info(name, uniqueid, prov):

   if prov == None:
      prov = "Canada"

   url = HOST +\
   GET_BUSINESS_DETAILS +\
   "prov=" + urllib.quote(prov.encode('utf8')) +\
   "&bus-name=" + urllib.quote(name.encode('utf8')) +\
   "&listingid=" + uniqueid +\
   "&fmt=" + FMT +\
   "&apikey=" + API_KEY +\
   "&UID=" + UNIQUE_ID

   conn = urllib2.urlopen(url,None)
   try:
      response = json.loads(conn.read())
   finally:
      conn.close()

   return response

"""
def main():
   result = search("Pizza","Montreal")
   business = result.get('listings')[0]
   time.sleep(1)
   print get_business_info(business.get('name'),business.get('id'),business.get('address.prov'))

if __name__ == "__main__":
   main()
"""   
