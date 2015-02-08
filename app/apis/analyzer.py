#!flask/bin/python
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
import yelp_api
import yellow_api
from dbchatter import getTwitterBall, BallExists

from alchemyapi_python import alchemyapi


T_CONSUMER_KEY = 'O9IiAWuqqs5GRWbMBBTgCI322'
T_CONSUMER_SECRET = '5a6BAdhFEuW3MBAt5AFdiaZwN7gyrk6TkaCLmmV6B5ydtzBoWv'
T_ACCESS_TOKEN = '54745215-vsvjElxhcznr0HTmpnJ3giGC3VkkiZFTjHI480hvY'
T_ACCESS_SECRET = '5ZdfmM2YxKEGCjmvOFGKWq5Sz6YATr1V7zbI8cYDWja48'

T_WEB_SEARCH_URL = 'https://www.twitter.com/search/?q='


def analyze(name, location, yelpstars, reviewcount, siteURL, yelpid):
    auth = tweepy.OAuthHandler(T_CONSUMER_KEY, T_CONSUMER_SECRET)
    auth.set_access_token(T_ACCESS_TOKEN, T_ACCESS_SECRET)

    api = tweepy.API(auth)

    place_id = api.reverse_geocode(location['lat'],location['long'])[0].id
    detail = api.geo_id(place_id).full_name

    if not BallExists(yelpid):

        print "Details of geocode " + str(detail)

        search_url = T_WEB_SEARCH_URL + 'place%3A'+place_id+'%20%22'+urllib.quote(name)+'%22'

        page = urllib2.urlopen(search_url)
        html = page.read()

        soup = BeautifulSoup(html)
        tweets = soup.find_all('p','js-tweet-text')
        tweet_texts = ""
        for i in range(len(tweets)):
          tweet_texts = tweet_texts + tweets[i].get_text().encode('ascii','ignore') + '\n'

        alchy = alchemyapi.AlchemyAPI()

        print tweet_texts

        final_result = alchy.sentiment_targeted('text',tweet_texts,name.lower())
        type = 'targeted'
        if final_result.get('status') == 'ERROR':
           final_result = alchy.sentiment('text',tweet_texts)
           type = 'general'
           print "Rerunning algo without targeted analysis. After second exec :" + str(final_result)
           if final_result['status'] =='ERROR':
               final_result="ERROR"
               return final_result



        final_result = final_result.get('docSentiment')
        if type == 'general':
            final_result['targeted'] = False
        else:
            final_result['targeted'] = True
        print final_result

        submitDB(name, location, detail, tweet_texts, final_result,yelpstars,reviewcount,siteURL,yelpid)

        return final_result
    else:
        return False

def submitDB(subname, sublocation, detail, subtweets, subresult,yelpstars, reviewcount, siteURL,yelpid):
    sub = models.TwitterBall(name=subname,lat=sublocation['lat'], long=sublocation['long'], locname=detail,
                             tweets=subtweets,ranking=subresult.get('type'),rankscore=subresult.get('score'),
                             ranktype=subresult.get('targeted'),yelpstars=yelpstars,yelpcount=reviewcount,
                             siteURL=siteURL,yelpid=yelpid)
    db.session.add(sub)
    db.session.commit()


def main():
   print analyze("Tony", {'lat': 40.722196, 'long': -73.987429})



if __name__ == "__main__":
   main()
