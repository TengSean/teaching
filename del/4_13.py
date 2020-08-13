#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:16:24 2020

@author: amanda
"""

import pandas as pd
import json
import datetime
from dateutil.relativedelta import* 
import time
import urllib.request


def getPriceData(ticker, start, end):
    start_timeArray = time.strptime(start,"%Y-%m-%d")
    start_timeStamp = int(time.mktime(start_timeArray))
    
print(start_timeStamp)
    end_timeArray = datetime.datetime.strptime(end,"%Y-%m-%d")
    end_timeArray +=datetime.timedelta(days=1)
    end_timeStamp = int(time.mktime(end_timeArray.timetuple()))

url = "https://query1.finance.yahoo.com/v7/finance/download/" + str(ticker) + ".TW?period1=" + str(start_timeStamp) + "&period2=" + str(end_timeStamp) + "&interval=1d&events=history"
urllib.request.urlretrieve(url, "./" + str(ticker) + ".csv")
with open("./20200331上課資料-3/backtest_targets_remove_delist_target.json","r")as f:
    target = json.load(f)
    for t in target[:10]: print(t)


bullish_return = []
bearish_return = []

'''target:

    'year': '100', 
    'month': '1',
    'bullish_target': '3406', 
    'bearish_target': '3535'
'''
for i in target:
    year = 1911 + int(i['year'])
    month = int(i['month'])
    DecemberOrNot = 12
    start, end = _, _
    #不用計算跨年
    if month != DecemberOrNot:
        startYear, endYear = str(year), str(year)
        startMonth, endMonth = str(month), str(month + 1)
        
        #月份不是二位數,要加0
        if month < 10:
            start = startYear + "-0" + str(startMonth) + "-11"
            end = endYear + "-0" + str(endMonth) + "-10"
        #月份是二位數,不要加0
        else:
            start = startYear + "-" + str(startMonth) + "-11"
            end = endYear + "-" + str(endMonth) + "-10"
    
    #要計算跨年
    else:
        print("year: " + i['year'])
        print("month: "+  i['month'])
        print("bullish_target: "+  i['bullish_target'])
        print("bearish_target: " + i['bearish_target'])
        start, end = str(year) + "-12-11", str(year+1) + "-01-10"
        print(start, end)
    break
try:
    getPriceData(i['bullish_target'], start, end)
    getPriceData(i['bearish_target'], start, end)
    #except:
        #TODO...
        break
    
file = open("bullish_return.pickle","wb")
pickle.dump(bullish_return,file)
file.close()
fire = open("bearish_return.pickle","wb")
file.close()

t=input("Plz enter ticker:")
s = input("Plz enter start time")
e = input("Plz enter end time")
print("your enter ticker is:{} start-time :{} end-time:{}".format(t, s ,e))


print(t, s, e)
getPriceData(t, s, e)

# print(start_timeStamp)

with open("backtest_targets.json","r")as f:
    target = json.load(f)
    
bullish_return = []
bearish_return = []

for i in range(0,len(target)):
    
    temp = target[i]
    ticker = t
    start = "2011-02-11"
    end = "2020-03-10"

getPriceData(ticker, start, end)

# print(start_timeStamp)
    temp["bullish_target_open_price"] = []
    temp["bullish_target_close_price"] = []
    temp["bearish_target_open_price"] = []
    temp["bearish_target_close_price"] = []
    
    if target[i]["bullish_target_open_price"] == "NaN" or \
       target[i]["bullish_target_close_price"] == "NaN" or \
       target[i]["bearish_target_open_price"] == "NaN" or \
       target[i]["bearish_target_close_price"] == "NaN":           
           continue
    bullish_return.append((target[i]["bullish_target_close_price"]- \
                       target[i]["bullish_target_open_price"])/ \
                      target[i]["bullish_target_open_price"])
    
    bearish_return.append((target[i]["bearish_target_open_price"]- \
                       target[i]["bearish_target_close_price"])/ \
                       target[i]["bearish_target_open_price"])
    
avg_return = sum(bullish_return+bearish_return)/len(bullish_return+bearish_return)

import pickle
file = open("bullish_return.pickle","wb")
pickle.dump(bullish_return,file)
file.close()

fire = open("bearish_return.pickle","wb")
pickle.dump(bullish_return.file)
file.close()



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
    r = requests.get(url)
    with open('./'+ticker+'.xls', 'wb') as f:
        f.write(r.content)
#     urllib.request.urlretrieve(url, "./data/price/2330.html")
    
t=input("Plz enter ticker:")
s = input("Plz enter start time")
e = input("Plz enter end time")
print("your enter ticker is:{} start-time :{} end-time:{}".format(t, s ,e))


print(t, s, e)
getPriceData(t, s, e)

# print(start_timeStamp)

trade_range = price_data.iloc[start_idx:end_idx]
trade_date_list = trade_range["Date"].tolist()
for i in range(0,len(trade_date_list)):
    trade_date_list[i]= datetime.datetime.strptime( trade_date_list[i], "%Y-%m-%d")
    
open_delta = []
close_delta = []
for i in range(0,len(trade_date_list)):
    open_delta.append(abs(trade data list[i]-open day))
    close_delta.append(abs(trade data list[i]-close day))
    
open_indices = [i for i x in enumerate(open_delta) if x == min(open_delta)]
close_indices = [i for i x in enumerate(close_delta) if x == min(close_delta)]

open_idx = open_indices[-1]
close_idx = close_indices[-1]

trade_range = trade_range.reset_index()
open_price = trade_range["Adj Close"][open_idx]
close_price = trade_range["Adj Close"][close_idx]




