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
UNIQUE_ID = 'pleyt'
FMT = 'JSON'
SEARCH_LIMIT = 10

FIND_BUSINESS = '/FindBusiness/?'
GET_BUSINESS_DETAILS = '/GetBusinessDetails/?'

#Search parameters


def search(term, location):

   url = HOST +\
   FIND_BUSINESS +\
   "what=" + urllib.quote(term.encode('utf8')) +\
   "&where=" + urllib.quote(location.encode('utf8')) +\
   "&pgLen=" + str(SEARCH_LIMIT) +\
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
def get_relevent_business_info(term, location):
   results = []
   listings = search(term,location)['listings']
   for listing in listings:
       b_info = get_business_info(listing['name'],listing['id'],listing['address']['prov'])
       relevant_info = { 'name':b_info['name'], 'urlname':b_info['name'].replace(" ","+"),'location':b_info['geoCode'],'rating':0,'numratings':0,'url':b_info['merchantUrl'],'categories':b_info['categories'] }
       results.append(relevant_info)
   return results
"""
def get_business_info(name, uniqueid, prov):

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

def shortsearch(term,location):
    """short search method to find businesses in area"""
    results = search(term,location)['businesses']
    result = []
    for business in results['listings']:
        result.append([business['id'],business['name']])
    return result

def main():
   print get_relevent_business_info("Pizza","Montreal")

if __name__ == "__main__":
   main() 
