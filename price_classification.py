# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:53:09 2018

@author: anujs
"""


import pandas as pd
from datetime import datetime

price = pd.read_csv('Bitcoin_Prices_April 11_May 11.csv',parse_dates=True)

price.drop([744,745],inplace=True)

delta_price = []


for i in range(1,len(price.index)):
    
     delta_price.append(price['Close Price'].loc[i] - price['Close Price'].loc[i-1])


delta_price.append(0)



#for x in range(0,744):

 #  print(delta_price[x])


delta_price_bin = []

#print(len(delta_price))

for j in delta_price:
    
    if j <=0:
        delta_price_bin.append(0)
    else:
        delta_price_bin.append(1)


price['Price Difference Class'] = delta_price_bin


print(price.tail())

price['Date'] = price['Date'].astype('datetime64[s]')

price.index = pd.to_datetime(price['Date'])

price.index = price.index.round('1H')

price.to_csv('Bitcoin Prices.csv')
