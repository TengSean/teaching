#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:01:11 2020

@author: amanda
"""




import datetime
import time
import urllib.request

def getPriceData(ticker, start, end):
    start_timeArray = time.strptime(start,"%Y-%m-%d")
    start_timeStamp = int(time.mktime(start_timeArray))
    
    print(start_timeStamp)
    end_timeArray = datetime.datetime.strptime(end,"%Y-%m-%d")
    end_timeArray +=datetime.timedelta(days=1)
    end_timeStamp = int(time.mktime(end_timeArray.timetuple()))
#     return start_timeStamp
    
#     this is comment
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + str(ticker) + ".TW?period1=" + str(start_timeStamp) + "&period2=" + str(end_timeStamp) + "&interval=1d&events=history"
    urllib.request.urlretrieve(url, "./data/price/" + str(ticker) + ".csv")
#     urllib.request.urlretrieve(url, "./data/price/2330.html")
    
# t = 0
# s = 0
# e = 0


######## get data ########
t = input("plz entrt ticker")
s = input("plz enter start-time")
e = 0
count = 3
while(count):
    e = input("plz enter end-time")
    if e > "2020-03-20":
        print("錯誤!!plz enter again")
        count -= 1
        # count = count - 1
    else:
#         print("yeah")
        break
    if count == 0:
        print("[error] you have entered wrong date")
        exit(1)
print("yea")


######## crawler ########
print(t, s, e)
getPriceData(t, s, e)

import matplotlib.pyplot as plt
import numpy as np


import plotly.graph_objects as go

import pandas as pd
from datetime import datetime
with open("./data/price","r")as f:
    target = json.load(f)
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.show()

