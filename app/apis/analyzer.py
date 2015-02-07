"""
Sentiment Analyzer that reads twitter feeds


@author David McVicar
"""

import tweepy
import urllib
import urllib2
import json
import re
from bs4 import BeautifulSoup
from app import db, models
from datetime import datetime

import yelp_api
import yellow_api
from alchemyapi_python import alchemyapi


T_CONSUMER_KEY = 'O9IiAWuqqs5GRWbMBBTgCI322'
T_CONSUMER_SECRET = '5a6BAdhFEuW3MBAt5AFdiaZwN7gyrk6TkaCLmmV6B5ydtzBoWv'
T_ACCESS_TOKEN = '54745215-vsvjElxhcznr0HTmpnJ3giGC3VkkiZFTjHI480hvY'
T_ACCESS_SECRET = '5ZdfmM2YxKEGCjmvOFGKWq5Sz6YATr1V7zbI8cYDWja48'

T_WEB_SEARCH_URL = 'https://www.twitter.com/search/?q='


def analyze(name, location):

    auth = tweepy.OAuthHandler(T_CONSUMER_KEY, T_CONSUMER_SECRET)
    auth.set_access_token(T_ACCESS_TOKEN, T_ACCESS_SECRET)

    api = tweepy.API(auth)

    place_id = api.reverse_geocode(location['lat'],location['long'])[0].id

    search_url = T_WEB_SEARCH_URL + 'place%3A'+place_id+'%20%22'+urllib.quote(name)+'%22'

    page = urllib2.urlopen(search_url)
    html = page.read()

    soup = BeautifulSoup(html)
    tweets = soup.find_all('p','js-tweet-text')
    tweet_texts = ""
    for i in range(len(tweets)):
      tweet_texts = tweet_texts + tweets[i].get_text().encode('ascii','ignore') + '\n'

    alchy = alchemyapi.AlchemyAPI()
    final_result = alchy.sentiment_targeted('text',tweet_texts,name)
    type = 'targeted'
    if final_result.get('status') == 'ERROR':
       final_result = alchy.sentiment('text',tweet_texts)
       type = 'general'
       print "Rerunning algo without targeted analysis. After second exec :" + str(final_result)

    final_result = final_result.get('docSentiment')
    if type == 'general':
        final_result['targeted'] = False
    else:
        final_result['targeted'] = True

    submitDB(name, location, tweet_texts, final_result)

    return final_result


   #print final_result['docSentiment']['type']
   #print final_result['docSentiment']['score']

def submitDB(subname, sublocation, subtweets, subresult=dict()):
    sub = models.TwitterBall(name=subname,latitude=sublocation['lat'], longitude=sublocation['long'], tweets=subtweets,
                             ranking=subresult.get('type'),
                             rankscore=subresult.get('score'), ranktype=subresult.get('targeted'), dateadded=datetime.now())
    db.session.add(sub)
    db.session.commit()


def main():
   print analyze("McDonalds", { 'lat': 40.722196, 'long': -73.987429})


if __name__ == "__main__":
   main()
