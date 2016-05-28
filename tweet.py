#!/usr/bin/env python3

import requests
from requests_oauthlib import OAuth1
import configparser 
import sys
import os

config = configparser.ConfigParser()
home = os.path.expanduser('~')
config.read(home + '/bin/twitter_info.ini')
my_info = dict()    
for option in config.options('twitter'):
    my_info[option] = config.get('twitter', option)

auth = OAuth1(my_info['app_key'],my_info['app_secret'],
              my_info['user_oath_token'],
              my_info['user_oath_token_secret'])   
session = requests.Session()
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
session.auth = auth
resp = session.get(url)
if resp.status_code != 200:
    print('Authentication failed')

new_tweet_lst = sys.argv[1:]
new_tweet = ""
for word in new_tweet_lst:
    new_tweet += word + " "
dic = {'status':new_tweet}
url2 = 'https://api.twitter.com/1.1/statuses/update.json'
resp = session.post(url2, data=dic)
if resp.status_code != 200:
    print('Failed to tweet')
