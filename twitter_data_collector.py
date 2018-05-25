# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:01:21 2018

@author: anujs
"""

import tweepy
import pandas as pd
from textblob import TextBlob

consumer_key = "clPBLLDHG5mTS5ffzAzaoNRm1"
consumer_secret = "scBlLPRjI4xtUfhgBu6joELfJOeOMxTI19CdqvrlXmmBEVu209"

access_key= "962177014311432192-CoXC8gXSe3jZPqLfmOz1W0nTg5PS6TI"
access_key_secret = "8VAR6phmtnzB3NVCbU8yKWleE8s5ZivQOqEZaH9OEVako"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_key_secret)
api=tweepy.API(auth)

result = []

for tweet in tweepy.Cursor(api.search,q='%23cryptocurrency',since='2018-05-23` 11:00:00').items(200):
    result.append(tweet)
    
print(len(result))

# Converting the JSON data to a Pandas dataframe

def todf(tweets):
    dataset = pd.DataFrame() #Empty dataframe
    
    dataset['tweet id']= [tweet.id for tweet in tweets]
    dataset['tweet_text'] = [tweet.text for tweet in tweets]
    dataset['Time'] = [tweet.created_at for tweet in tweets]
    dataset['userTimezone'] = [tweet.user.time_zone for tweet 
    in tweets]
    return dataset

dataset = todf(result)


print(dataset.info())
print(dataset['Time'])

dataset.to_csv('Tweets_May23_timecontrolled.csv')

