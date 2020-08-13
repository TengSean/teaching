#!/usr/bin/env python
# coding: utf-8

# In[16]:

import os

os.environ['PATH'] = os.environ['PATH'] + ':/Users/amanda/Downloads/'
if 'chromedriver' in os.environ['PATH']:
    print('Environment var setting successfully!')



from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import Select


import time
import numpy as np
import pandas as pd
import os

abspath = os.path.abspath(r"/Users/amanda/Downloads/chromedriver")
abspath = r"/Users/amanda/Downloads/chromedriver"
def crawler(ticker, sd, ed):
    sdList = sd.split('-')
    edList = ed.split('-')
    sdList[0] = int(sdList[0]) - 1911
    edList[0] = int(edList[0]) - 1911
    sdList[0], edList[0] = str(sdList[0]), str(edList[0])
    sd = ''.join(sdList)
    ed = ''.join(edList)
    
    dateList = []
    chrome_options = Options()
    chrome_options.add_argument("--headless")       # define headless

    # add the option when creating driver
#    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
#     driver = webdriver.Chrome()

    driver.get("https://mops.twse.com.tw/mops/web/STAMAK03_1")
    # time.sleep(1)
    driver.find_element_by_id("co_id").click()
    driver.find_element_by_id("co_id").clear()
    driver.find_element_by_id("co_id").send_keys(ticker)
    driver.find_element_by_id("b_date").click()
    driver.find_element_by_id("b_date").clear()
    driver.find_element_by_id("b_date").send_keys(sd)
    driver.find_element_by_id("e_date").click()
    driver.find_element_by_id("e_date").clear()
    driver.find_element_by_id("e_date").send_keys(ed)
    time.sleep(0.5)
    driver.find_element_by_id("nav02").click()
    driver.find_element_by_xpath(u"//input[@value=' 查詢 ']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//img[@alt='開新視窗']").click()

    html = driver.page_source

    bs4 = BeautifulSoup(html)

    table = bs4.find_all('table', {'class':'hasBorder'})
    if len(table) == 0:
        print('There are no data.')
        return dateList, []
    table = table[0].find_all('td')
    tmpList = list()
    dataNP = []
    for i, t in enumerate(table):
        tmpList.append(t.text)
        if i % 11 == 10 and i == 10:
            dataNP = tmpList
            tmpList = list()
        elif i % 11 == 10:
            tmpList = np.array(tmpList)[None,:]
            dataNP = np.vstack((dataNP, tmpList))
            tmpList = list()
    df = pd.DataFrame(dataNP)
    colName = ['公司代號',	'公司名稱',	'設質人身份別',	'設質人姓名',	'質設異動發生日期',	'設質股數',	'解質股數',	'累積質設股數',	'質權人姓名',	'備註',	'申報日期']
    df.columns = colName
    df = df.drop(columns=['公司代號', '公司名稱', '備註'])
#     display(df)
#     print(df.loc[df['解質股數'] !=0])
    return dateList, df


# In[23]:


import datetime
import plotly.graph_objects as go
    
def plotCandle(df, ticker, dateList):
    ymax = max(df['High'].tolist()) + 20
    ymin = min(df['Low'].tolist()) - 20
#     print(dateList)
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'], high=df['High'],
                    low=df['Low'], close=df['Close'])])
    for d in dateList:
        if d[3]:
            c = 'LightSeaGreen'
        else:
            c = 'red'
        fig.add_shape(
                type="rect",
                x0=d[0],
                y0=ymin,
                x1=d[1],
                y1=ymax,
                fillcolor=c,
                opacity = 0.5,
                layer = 'below',
                line_width = 0
        )
    fig.update_layout(xaxis_rangeslider_visible=False,
                      title='Dailt candlestick of {}'.format(ticker),
                     )
    fig.show()
    tLock, fLock = True, True
    ma, mi = 0.0, 0.0
    maC, miC = 0, 0
    for d in dateList:
        if d[3] and tLock:
            print('設質的最高投報率與時間區間(綠色)')
            print('_'*20)
            tLock = False
        elif not d[3] and fLock:
            print('\n解質的最低投報率與時間區間(紅色)')
            print('_'*20)
            fLock = False
        if fLock:
#             print('demo: {}'.format(d[2]))
            maC+=1
            ma+=d[2]
        else:
#             print('demo: {}'.format(d[2]))
            miC+=1
            mi+=d[2]
        print('{} - {} : {}'.format(d[0], d[1], d[2]))
    print('\nSummary')
    print('_'*20)
    maThres = 0.1
    miThres = 0.0
    if maC > 0:
        print('Avg 設質 (期望 {}): {}'.format(maThres, ma/maC))
        if ma/maC > maThres:
            print('評語： 不錯')
        else:
            print('評語: 似乎不這摸好....')
    if miC > 0:
        print('Avg 解質 (期望 {}): {}'.format(miThres, mi/miC))
        if mi/miC < miThres:
            print('評語： 不錯')
        else:
            print('評語: 似乎不這摸好....')
        
def getApproxDate(ticker, start, end):
    
    tickerPath = os.path.join(DIR, ticker+'.csv')
    
    start = datetime.datetime.strptime( start, "%Y-%m-%d")
    end = datetime.datetime.strptime( end, "%Y-%m-%d")
    # 先取列的範圍: start_idx ~ end_idx (ex: 2011-02-08 ~ 2011-03-31)
    # 再取行的範圍 (hint: 指取date得部份)
    df = pd.read_csv(tickerPath)
    trade_date_list = df["Date"].tolist()
#     trade_date_list = trade_range['Date'].tolist()
    # display(trade_range)

    for i in range(0, len(trade_date_list)):
        trade_date_list[i] = datetime.datetime.strptime( trade_date_list[i], "%Y-%m-%d")

    # 計算2月到3月之間跟open_day與close_day的差距...
    open_delta = []
    close_delta = []
    for i in range(0, len(trade_date_list)):
#         print(abs(trade_date_list[i] - open_day))
    #     break
        open_delta.append( abs( trade_date_list[i] - start) )
        if trade_date_list[i] <= end:
            close_delta.append(abs(trade_date_list[i] - end))
#         Amanda version.
#         else:
#             continue
#             print(trade_date_list[i])

    open_indices = [ i for i, x in enumerate(open_delta) if x == min(open_delta)]
    close_indices = [ i for i, x in enumerate(close_delta) if x == min(close_delta)]
    
    '''
    
        open_day = 2011-02-11
        假設今天沒有2011-02-11但是有2011-02-10, 2011-02-12
        由此可知上述兩個日期與2011-02-11的差距皆為1,但我們要找的是2011-02-11～2011-03-10的間距
        故2011-02-10這個日期不是我們要的
    
    ''' 
    open_idx = open_indices[-1]
    close_idx = close_indices[-1]
    
#     display(df.iloc[open_idx:close_idx])
    subDF = df.iloc[open_idx:close_idx]
    date = subDF["Date"].tolist()
    sd, ed = date[0], date[-1]
    
    dateList, redf = crawler(ticker, sd, ed)
    plotCandle(subDF, ticker, dateList)
    return dateList, redf, subDF


# In[24]:


import os

DIR = './data/price'
tickerList = os.listdir(DIR)
ticker = None
start = None
end = None
# ticker = '9928'
# start = '2011-03-02'
# end = '2011-05-11'
# ticker = '4994'
# start = '2011-01-01'
# end = '2020-01-31'
while(1):
    ticker = input('Plz input the ticker(ex:4994): ')
    if ticker +".csv" not in tickerList:
        print('Can\'t find this ticker.')
        continue
    start = input('Plz input the start date(ex:2011-01-01): ')
    end = input('Plz input the end date(ex:2020-01-31): ')
    break
dateList, redf, subDF = getApproxDate(ticker, start, end)
if len(redf) == 0:
#     plotCandle(subDF, ticker, dateList)
    print('此公司無此資料')
    exit(0)


# In[25]:


pd.set_option('display.max_rows', 999)

piror = [
    '董事長', '董事長配偶', '董事本人', '董事之法人代表人', 
    '大股東本人', '大股東利用他人名義', 
    '總經理', '副總經理本人', '副總經理利用他人名義持有者', 
    '監察人本人' 
]

colName = redf.columns.tolist()
# print(colName)

def dateConvert1(date):
    tmp = []
    for idx, d in enumerate(date.split('/')):
        if idx == 0:
            tmp.append(str(int(d) + 1911))
        else:
            tmp.append(d)
    return '-'.join(tmp)
def dateConvert2(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d')
#     print(date)
redf['質設異動發生日期'] = pd.Series(map(dateConvert1, redf['質設異動發生日期'].tolist()))
# dateConvert2 = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d')
redf['date'] = list(map(dateConvert2, redf['質設異動發生日期'].tolist()))
# display(redf)
# print(pd.Series(map(dateConvert, redf['質設異動發生日期'].tolist())))


# In[26]:


import copy
def getDate(redf):
#     print(redf.shape[0])
    if redf.shape[0] == 0:
        return list()
#     if redf.shape[0]:
    
    ll = redf['date'].tolist()
    rel = ll[::-1]
    checkl = copy.deepcopy(rel)
    threshold = rel[0]
    for idx, l in enumerate(rel):

        diff = threshold - l
    #     print(idx, diff)
        if diff == datetime.timedelta(days = 0):
            if idx - 1 > 0 and rel[idx] == rel[idx-1]:
    #             print('threshold: {} current: {} ,diff=0, False'.format(threshold, l))
                checkl[idx] = False
            else:
    #             print('threshold: {} current: {} ,diff=0, True'.format(threshold, l))
                checkl[idx] = True
    #         checkl[idx] = True  
        elif diff < datetime.timedelta(days=90):
    #         print('threshold: {} current: {}  ,diff<90, False'.format(threshold, l))
            checkl[idx] = False
        else:
    #         print('threshold: {} current: {}  ,diff>90, True'.format(threshold, l))
    #         print('>90')
            # equal to zero
            checkl[idx] = True
            threshold = l
    #         print(l[idx] - l[idx+1])
    checkl = np.asarray(checkl)
#     print(checkl)
#     List1 = redf.loc[checkl]['質設異動發生日期'].tolist()
#     List2 = redf.loc[checkl]['date'].tolist()
#     result = []
#     for i in range(len(List1)):
#         result.append([List1[i], List2[i]])
#     print(len(result), len(List1))
#     return result
    return redf.loc[checkl]['date'].tolist()
# getDate(redf)


# In[27]:


def calMoney(df, lock):
#     print(df.shape)
    df.dropna(axis='rows')
#     display(df)
    adjList = []
    for x, y in zip(df['Date'].tolist(), df['Adj Close'].tolist()):
        adjList.append([x, y])
#     print(adjList)
#     print(adjList)
#     adjList = [ df['Date'].tolist(), df['Adj Close'].tolist() ]
#     print(adjList)
    maxIndex, maxValue = 0, -999.9
    minIndex, minValue = 0, 100.0
#     print(len(adjList))
    for i in range(1, len(adjList)):
#         print(i)
#         print(adjList[i][1])
        tmp = (float(adjList[i][1]) - float(adjList[0][1])) / float(adjList[0][1])
#         print(tmp)
        if lock:
            if tmp > maxValue:
                maxIndex, maxValue = i, tmp
        else:
            if tmp < minValue:
                minIndex, minValue = i, tmp
#     print('indx: {}, maxval: {}'.format(maxIndex, maxValue))
    if lock:
        return [ adjList[0][0], adjList[maxIndex][0], maxValue, lock]
    else:
        return [ adjList[0][0], adjList[minIndex][0], minValue, lock]

    #     print('------')
def getApproxDate2(st, end, subDF, lock):
    '''
    st = 	2020-01-03
    end = 	2020-02-03
    subDF = 開收盤df
    lock-> True: 設質
           False:解質
    '''
#     start = datetime.datetime.strptime( st, "%Y-%m-%d")
#     end = datetime.datetime.strptime( end, "%Y-%m-%d")
    # 先取列的範圍: start_idx ~ end_idx (ex: 2011-02-08 ~ 2011-03-31)
    # 再取行的範圍 (hint: 指取date得部份)
#     df = pd.read_csv(tickerPath)
#     print(st, end)
    trade_date_list = subDF["Date"].tolist()
#     trade_date_list = trade_range['Date'].tolist()
    # display(trade_range)

    for i in range(0, len(trade_date_list)):
        trade_date_list[i] = datetime.datetime.strptime( trade_date_list[i], "%Y-%m-%d")

    # 計算2月到3月之間跟open_day與close_day的差距...
    open_delta = []
    close_delta = []
    for i in range(0, len(trade_date_list)):
        open_delta.append( abs( trade_date_list[i] - st) )
        if trade_date_list[i] <= end:
            close_delta.append(abs(trade_date_list[i] - end))

    open_indices = [ i for i, x in enumerate(open_delta) if x == min(open_delta)]
    close_indices = [ i for i, x in enumerate(close_delta) if x == min(close_delta)]
    
    '''
    
        open_day = 2011-02-11
        假設今天沒有2011-02-11但是有2011-02-10, 2011-02-12
        由此可知上述兩個日期與2011-02-11的差距皆為1,但我們要找的是2011-02-11～2011-03-10的間距
        故2011-02-10這個日期不是我們要的
    
    ''' 
    open_idx = open_indices[-1]
    close_idx = close_indices[-1]
#     print(open_idx, close_idx)
    tmpDF = subDF.iloc[open_idx:close_idx]
    return tmpDF
#     display(tmpDF)
#     date = tmpDF["Date"].tolist()
#     sd, ed = date[0], date[-1]
#     print(sd, ed)
#     dateList, redf = crawler(ticker, sd, ed)
#     plotCandle(subDF, ticker, dateList)
#     return dateList, redf, subDF
    
    


# In[28]:


def dateHandler(dateList, subDF, lock):
    returnList = []
    if len(dateList) != 0:
        for s in dateList:
#             print('Current Date: {}'.format(s))
            st = s
            end = st + datetime.timedelta(days=70)
            tmpDF = getApproxDate2(st, end, subDF, lock=lock)
#             getcal = calMoney(tmpDF, lock=True)
            returnList.append(calMoney(tmpDF, lock=lock))
#         print(len(resultList))
#         print(returnList)
        return returnList
        
#             print(resultList)
#             print(end)
#             end = time.strftime("%Y-%m-%d", end)
#             print(st.date(), end.date(), end - st)
    else:
#         print('no date')
        return []

indexList = []
for p in piror:
    indexList = redf.index[redf["設質人身份別"].str.find(p )!= -1]
    if len(indexList) != 0:
        break
# indexList = redf.index[redf["設質人身份別"].str.find(piror[4]) != -1]

pirorDf = redf.loc[indexList]
# display(pirorDf)
pirorName =list(set(pirorDf['設質人姓名']))
text2int = lambda x: int(x.strip().replace(',',''))
dateConvert = lambda x: [ xx for idx, xx in enumerate(x.split('/')) if idx == 0]
# print(pirorName)

for pn in pirorName:
    resultList = []
#     print('Current name: {}'.format(pn))
#     print('aa')
    pnDf = pirorDf.loc[pirorDf['設質人姓名'] == pn]
    setIndex = pd.Series(map(text2int, pnDf['設質股數'])) != 0
    disIndex = pd.Series(map(text2int, pnDf['解質股數'])) != 0
    setIndex = np.asarray(setIndex)
    disIndex = np.asarray(disIndex)
#     print(type(pnDf.index[pnDf['設質股數'] !='0'].values))
    setNum = pnDf[setIndex]
    disNum = pnDf[disIndex]
#     display(setNum)
#     display(disNum)
    setDate = getDate(setNum)
    disDate = getDate(disNum)
    plotList = []
    plotList.extend(dateHandler(setDate, subDF, lock=True))
    plotList.extend(dateHandler(disDate, subDF, lock=False))
#     print(plotList)
    plotCandle(subDF, ticker, plotList)
    


# In[177]:


# # time = '2001/06/26'

# # datetime.datetime.strptime(tt['質設異動發生日期'], "%Y-%m-%d")
# datet = lambda x: datetime.datetime.strptime(x, "%Y-%m-%d")
# for ttt in tt['質設異動發生日期'].tolist():
#     print(datetime.datetime.strptime(ttt, "%Y-%m-%d"))
# # pd.Series(map(datet, tt['質設異動發生日期'].tolist()))
# # datetime.datetime.strptime(time, "%Y-%m-%d")


# In[ ]:




