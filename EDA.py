# -*- coding: utf-8 -*-
"""
Created on Fri May 25 02:58:44 2018

@author: anujs
"""

import pandas as pd
from textblob import TextBlob
from datetime import datetime,timedelta
import matplotlib.pyplot as plt


tweet = pd.read_csv('combined.csv',parse_dates=True)
price = pd.read_csv('Bitcoin Prices.csv')


tweet['Time'] = tweet['Time'].astype('datetime64[s]')

tweet.index = pd.to_datetime(tweet['Time']- timedelta(hours=1))
tweet.index = tweet.index.round('1H')

price['Date'] = price['Date'].astype('datetime64[s]')

price.index = pd.to_datetime(price['Date'])

price.index = price.index.round('1H')

senti = []

for i in tweet['tweet_text']:
    
    
    senti.append(TextBlob(i).polarity)
    

tweet['Sentiment'] = senti


count_0 = 0
count_pos = 0
count_neg =0

for j in senti:
    
    if j==0:
        count_0+=1
        
    elif j>0:
        
    
        count_pos+=1
    else :
        
        count_neg+=1


print('\n Neutral Sentiment :' + str(count_0))

print('\n Positive Sentiment :' + str(count_pos))

print('\n Negative Sentiment :' + str(count_neg))

senti_list = [count_0,count_pos,count_neg]

df = tweet.merge(price,left_index=True,right_index=True,how='inner')


df.drop(['Date','Date.1','Time'],axis=1,inplace=True)

print(df.head())

plt.hist(df['Sentiment'])
plt.xlabel('Sentiment')
plt.ylabel('Frequemcy')
plt.title('Frequency of Sentiments')
plt.xticks(rotation=60)
plt.show()

plt.scatter(df['Sentiment'],df['Price Difference Class'])
plt.xlabel('Sentiment')
plt.ylabel('Price Difference Class')
plt.title('Sentiment vs Price Class')
plt.show()


plt.pie(senti_list,labels=['Neutral','Positive','Negative'])
plt.title('Pie chart of Sentiment split')
plt.show()

