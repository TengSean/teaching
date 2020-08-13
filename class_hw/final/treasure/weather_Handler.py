#!/usr/bin/env python
# coding: utf-8

# In[98]:


import requests

import os, sys
import json
import pickle
import urllib


# In[94]:

'''
為一個儲存天氣資訊的物件, 也是儲存的單位(檔名預設為日期)
'''
class weather_Factor():
    def __init__(self, ):
        '''
            Fill something here 
            api link: https://opendata.cwb.gov.tw/dist/opendata-swagger.html
            doc: https://opendata.cwb.gov.tw/opendatadoc/MFC/D0047.pdf
        '''
        self.__factor = {
            '天氣氣象': None,
            '降雨機率': None,
            '最高溫度': None,
            '最低溫度': None,
            '舒適度':  None,
            'Date': None

        }
#         print(self.__factor)
    # 設定天氣狀況
    def set_Wx(self,value):
        #print('[INFO] set_Wx function testing')        
        self.__factor['天氣氣象'] = value

    # 設定降雨機率
    def set_PoP(self,value):
        #print('[INFO] set_PoP function testing')
        self.__factor['降雨機率'] = value

    # 設定當天最高溫度
    def set_MaxT(self, value):
        #print('[INFO] set_MaxT function testing')
        self.__factor['最高溫度'] = value
    
    # 設定當天最低溫度
    def set_MinT(self, value):
        #print('[INFO] set_MinT function testing')
        self.__factor['最低溫度'] = value

    # 設定天氣舒適度
    def set_CI(self, value):
        #print('[INFO] set_CI function testing')
        self.__factor['舒適度'] = value
    
    # 設定日期
    def set_Date(self, date):
        #print('[INFO] set_Date function testing')
        self.__factor['Date'] = date
    
    # 取得天氣狀況
    def get_Wx(self,):
        #print('[INFO] get_Wx function testing')        
        return self.__factor['天氣氣象']

    # 取得降雨機率
    def get_PoP(self,):
        #print('[INFO] get_PoP function testing')
        return self.__factor['降雨機率']
    
    # 取得最高溫度
    def get_MaxT(self, ):
        #print('[INFO] get_MaxT function testing')
        return self.__factor['最高溫度']
    
    # 取得最低溫度
    def get_MinT(self, ):
        #print('[INFO] get_MinT function testing')
        return self.__factor['最低溫度']
    
    # 取得天氣舒適度
    def get_CI(self, ):
        #print('[INFO] get_CI function testing')
        return self.__factor['舒適度']

    # 取得日期
    def get_Date(self,):
        #print('[INFO] get_Date function testing')        
        return self.__factor['Date']
    


# In[128]:


'''
weather_Handler為一個跟weather_Factor互動得界面
參數為 縣市 ex: 新竹市 新北市 高雄市, etc
'''
class weather_Handler():
    def __init__(self, town):
        self.weather_dict = {
            'Wx':['天氣氣象', self.__Wx_handler],
            'PoP':['降雨機率', self.__PoP_handler],
            'MaxT':['最低溫度', self.__MaxT_handler],
            'MinT':['舒適度', self.__MinT_handler],
            'CI':['最高溫度', self.__CI_handler]
        }
        self.__current_Date=''
        self.url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-CFFF5EE8-F970-4123-8D43-86C2EF4BC4F9&locationName=' + urllib.parse.quote(town)
        self.__factor = weather_Factor()
        self.__start()
    def __start(self, ):
        #print('[INFO] __start function testing')
        self.__request_handler()
    '''
    Sample:

      "records": {
        "datasetDescription": "三十六小時天氣預報",
        "location": [
          {
            "locationName": "新竹市",
            "weatherElement": [
              {
                "elementName": "Wx",
                "time": [
                  {
                    "startTime": "2020-06-06 18:00:00",
                    "endTime": "2020-06-07 06:00:00",
                    "parameter": {
                      "parameterName": "多雲時陰短暫陣雨或雷雨",
                      "parameterValue": "16"
                    }
                  },{ ... }]
                }
                ]
            }
        ]
        },
    '''
    # 爬天氣資料
    def __request_handler(self, ):
        #print('[INFO] __request_handler function testing')
        response = requests.get(self.url)
        rtext = response.text
        json_response = rtext if self.__json_check(rtext) else self.__json_transfer(rtext)
        json_response = json_response['records']['location'][0]['weatherElement']
#         self.__Date_handler(json)
        for j in json_response:
            j_value = j['time'][0]
            if self.__factor.get_Date() == None:
                self.__Date_handler(j_value)
            self.weather_dict[j['elementName']][1](j_value)
    # 檢查檔案是否為json格式（爬下來的資料可能是str）
    def __json_check(self, rtext):
        #print('[INFO] json_check function testing')
        return True if isinstance(rtext, dict) else False
    # 將檔案轉成json
    def __json_transfer(self, rtext):
        #print('[INFO] json_transfer function testing')
        return json.loads(rtext)
    
    
    '''
    sample: {   'startTime': '2020-06-06 18:00:00', 
                'endTime': '2020-06-07 06:00:00',
                'parameter': {
                        'parameterName': '多雲時陰短暫陣雨或雷雨',
                        'parameterValue': '16'
                            }
            }
    '''
    # 處理天氣狀況資訊
    def __Wx_handler(self,j_value):
        '''
        'parameterName': '多雲時陰短暫陣雨或雷雨',
        'parameterValue': '16'
        '''
#         self.__Date_handler(j_value)
        #print('[INFO] __Wx_handler function testing')
        parameterName = j_value['parameter']['parameterName']
        self.__factor.set_Wx(parameterName)
        #print(self.__factor.get_Wx())
    # 處理降雨機率資訊
    def __PoP_handler(self, j_value):
        '''
        'parameterName': '30',
        'parameterUnit': '百分比'
        '''
        #print('[INFO] __PoP_handler function testing')
#         print(j_value['parameter'])
        parameterName = j_value['parameter']['parameterName'] + "%"
        self.__factor.set_PoP(parameterName)
        #print(self.__factor.get_PoP())
    # 處理最低溫度資訊
    def __MinT_handler(self, j_value):
        '''
        'parameterName': '27',
        'parameterUnit': 'C'
        '''
        #print('[INFO] __MinT_handler function testing')
#         print(j_value['parameter'])
        parameterName = j_value['parameter']['parameterName'] + "°C"
        self.__factor.set_MinT(parameterName)
        #print(self.__factor.get_MinT())

    # 處理最高溫度資訊
    def __MaxT_handler(self, j_value):
        '''
        'parameterName': '30',
        'parameterUnit': 'C'
        '''
        
        #print('[INFO] __MaxT_handler function testing')
#         print(j_value['parameter'])
        parameterName = j_value['parameter']['parameterName'] + "°C"
        self.__factor.set_MaxT(parameterName)
        #print(self.__factor.get_MaxT())

    # 處理天氣舒適度資訊
    def __CI_handler(self, j_value):
        '''
        'parameterName': '舒適至悶熱'
        '''
        #print('[INFO] __CI_handler function testing')
#         print(j_value['parameter'])
        parameterName = j_value['parameter']['parameterName']
        self.__factor.set_CI(parameterName)
        #print(self.__factor.get_CI())
    
    # 處理日期資訊
    def __Date_handler(self, j_value):
        '''
        'parameterName': '舒適至悶熱'
        '''
        #print('[INFO] __Date_handler function testing')
        date = j_value['startTime']
        date = date.replace('-', '').split(' ')[0]
        self.__factor.set_Date(date)
        #print(self.__factor.get_Date())
#         parameterName = j_value['parameter']['parameterName']
#         self.__factor.set_CI(parameterName)
#         print(self.__factor.get_CI())
    
    # 取得天氣狀況資訊 （呼叫 weather_Factor的get_Wx）
    def get_Wx(self,):
        #print('[INFO] get_Wx function testing')
        return self.__factor.get_Wx()

    # 取得降雨機率資訊 （呼叫 weather_Factor的get_PoP）
    def get_PoP(self,):
        #print('[INFO] get_PoP function testing')
        return self.__factor.get_PoP()

    # 取得最低溫度資訊 （呼叫 weather_Factor的get_MinT）
    def get_MinT(self, ):
        #print('[INFO] get_MinT function testing')
        return self.__factor.get_MinT()

    # 取得最高溫度資訊 （呼叫 weather_Factor的get_MaxT）
    def get_MaxT(self, ):
        #print('[INFO] get_MaxT function testing')
        return self.__factor.get_MaxT()

    # 取得天氣舒適度資訊 （呼叫 weather_Factor的get_CI）
    def get_CI(self, ):
        #print('[INFO] get_CI function testing')
        return self.__factor.get_CI()

    # 取得日期資訊 （呼叫 weather_Factor的get_Date）
    def get_Date(self, ):
        #print('[INFO] get_Date function testing')
        return self.__factor.get_Date()
    # 讀取pickle檔（weather_Factor）
    # 參數為檔案名稱（str）
    def load_pickle(self, filename):
        #print('[INFO] load_pickle function testing')
        DIR = os.path.join('./data/weather', filename)
        with open(DIR, 'rb') as f:
            self.__factor = pickle.load(f)
    # 儲存pickle檔（weather_Factor）
    def save_pickle(self, ):
        #print('[INFO] save_pickle function testing')
        if os.path.exists('./data/weather'):
            print('exits')
        else:
            print('not exist')
            if not os.path.exists('./data'):
                os.mkdir('./data')
            os.mkdir('./data/weather')
        DIR = os.path.join('./data/weather', self.__factor.get_Date()) + '.pkl'
        #print(DIR)
        with open(DIR, 'wb') as f:
            pickle.dump(self.__factor, f)


# In[132]:


town = input('請輸入縣市(Ex: 新竹市)')


# In[133]:


wh = weather_Handler(town)
# print(wh.get_Wx())
wh.save_pickle()

# wh.load_pickle('20200606.pkl')
print(wh.get_Wx())
print(wh.get_PoP())
print(wh.get_MinT())
print(wh.get_MaxT())
print(wh.get_CI())
print(wh.get_Date())


# In[ ]:




