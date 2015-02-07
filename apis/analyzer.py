"""
Sentiment Analyzer that reads twitter feeds

@author David McVicar
"""

import requests
import base64

import yelp_api
import yellow_api
from alchemyapi_python import alchemyapi.py

T_CONSUMER_KEY = 'O9IiAWuqqs5GRWbMBBTgCI322'
T_CONSUMER_SECRET = '5a6BAdhFEuW3MBAt5AFdiaZwN7gyrk6TkaCLmmV6B5ydtzBoWv'



def analyze(name, location):
    twitter_key = T_CONSUMER_KEY + ':'  + T_CONSUMER_SECRET
    header = { "Host" : "api.twitter.com",\
               "User Agent": "mouthfeel",\
               "Authorization" : "Basic " + base64.b64encode(twitter_key),\
               "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8"
               
