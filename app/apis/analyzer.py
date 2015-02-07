"""
Sentiment Analyzer that reads twitter feeds

@author David McVicar
"""

import requests
import base64
import json

import yelp_api
import yellow_api
from alchemyapi_python import alchemyapi

T_AUTH_URL = 'https://api.twitter.com/oauth2/token'
T_GEO_SEARCH_URL = 'https://api.twitter.com/1.1/geo/search.json'
T_CONSUMER_KEY = 'O9IiAWuqqs5GRWbMBBTgCI322'
T_CONSUMER_SECRET = '5a6BAdhFEuW3MBAt5AFdiaZwN7gyrk6TkaCLmmV6B5ydtzBoWv'



def analyze(name, address):

    #Get the Application-onlu bearer Token
    twitter_key = T_CONSUMER_KEY + ':'  + T_CONSUMER_SECRET
    headers = {"Authorization" : "Basic " + base64.b64encode(twitter_key),\
               "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8" }
    payload = { "grant_type" : "client_credentials" }

    
    r = requests.post(T_AUTH_URL,data=payload,headers=headers)
    token = r.json().get('access_token')

    print token

    #Run Twitter geo location query
    payload = { "query" : name , "attribute:street_address" : address }
    headers = { "Authorization" : "Bearer " + token }

    r = requests.get(T_GEO_SEARCH_URL,params=payload,headers=headers)
    print r
    matches = r.json()
    print matches

def main():
   analyze("Double Pizza","1146 boul. Marcel-Laurin")

if __name__ == "__main__":
   main()
