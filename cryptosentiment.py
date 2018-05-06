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

for tweet in tweepy.Cursor(api.search,q='%23Bitcoin').items(500):
    result.append(tweet)
    
print(len(result))

# Converting the JSON data to a Pandas dataframe

def todf(tweets):
    dataset = pd.DataFrame() #Empty dataframe
    
    dataset['tweet id']= [tweet.id for tweet in tweets]
    dataset['tweet_text'] = [tweet.text for tweet in tweets]
    
    return dataset

dataset = todf(result)

print(dataset.head())



#for para in dir(public_tweet[0]):
 #   print(para,eval('public_tweet[0].'+para))

#for tweet in public_tweet:  # Creates a string obj
 #   print(tweet.text) 
  #  print(TextBlob(tweet.text).polarity)