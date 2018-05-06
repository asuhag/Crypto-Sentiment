# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 01:37:31 2018

@author: anujs
"""

import pandas as pd

price = pd.read_csv('coindesk.csv')

print(price['Close Price'].loc[1])

delta_price = [i-price['Close Price'].mean() for i in price['Close Price'] ]   

print(delta_price)