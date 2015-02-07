"""
Sentiment Analyzer that reads twitter feeds

@author David McVicar
"""

import tweepy
import urllib
import oauth2

import yelp_api
import yellow_api
from alchemyapi_python import alchemyapi


T_CONSUMER_KEY = 'O9IiAWuqqs5GRWbMBBTgCI322'
T_CONSUMER_SECRET = '5a6BAdhFEuW3MBAt5AFdiaZwN7gyrk6TkaCLmmV6B5ydtzBoWv'
T_ACCESS_TOKEN = '54745215-vsvjElxhcznr0HTmpnJ3giGC3VkkiZFTjHI480hvY'
T_ACCESS_SECRET = '5ZdfmM2YxKEGCjmvOFGKWq5Sz6YATr1V7zbI8cYDWja48'

T_WEB_SEARCH_URL = 'https://twitter.com/search'


def analyze(name, location):

   auth = tweepy.OAuthHandler(T_CONSUMER_KEY, T_CONSUMER_SECRET)
   auth.set_access_token(T_ACCESS_TOKEN, T_ACCESS_SECRET)

   api = tweepy.API(auth)

   place_id = api.reverse_geocode(location.get('lat'),location.get('long'))[0].id

   #tweets = api.search(q = 'place%3A'+place_id+'%20%22'+urllib.quote(name)+'%22')
   tweets = api.search(q = 'Pizza')
   print 'place%3A' + place_id + '%20%22' + urllib.quote(name) + '%22'
   print tweets

   alchy = alchemyapi.AlchemyAPI()
   #final_result = alchy.sentiment_targeted('url',search_url,name)
   

def main():
   analyze("Starbucks",{ 'lat' : 37.2304516, 'long' : -80.4294548})


if __name__ == "__main__":
   main()
