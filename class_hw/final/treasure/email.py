#!/usr/bin/env python
# coding: utf-8

# In[20]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import ssl

import os


# In[21]:


class User():
    def __init__(self, address, password):
        self.address = address
        self.password = password
    # 設定發送方的 address password    
    def set_user(self, address, password):
        self.user = address
        self.password=password
    
    # 取得address
    def get_address(self, ):
        return self.address

    # 取得password
    def get_password(self, ):
        return self.password


# In[29]:


class send_Mail():
    def __init__(self, address=None, password=None):
        self.user=User(address, password)
        self.mail = MIMEMultipart()
        self.to_address = []
        self.subject = 'Sending email testing'
        self.contents = '''
                This is a demo message.
                        '''
        self.attachment = []
    # 當你已經準備要發送信件就呼叫這個function
    # 發送前請確定contents subject已經做完更動 否則會以default為主
    # 參數為接收方的address(list)
    def send(self, address):
        self.__set_mail(address)
        self.__set_attach()
        smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpserver.ehlo()
        smtpserver.login(self.user.get_address(), self.user.get_password())
        smtpserver.sendmail(self.user.get_address(), self.to_address, self.mail.as_string())
        smtpserver.quit()
    # mail object setting
    def __set_mail(self, address):
        self.to_address.extend(address)
        print(self.attachment)
        self.mail['From'] = self.user.get_address()
        self.mail['To'] = ', '.join(self.to_address)
        self.mail['Subject'] = self.subject
        self.mail.attach(MIMEText(self.contents))
    # attachment setting
    def __set_attach(self, ):
        if not len(self.attachment) == 0:
            for file in self.attachment:
                with open(file, 'rb') as f:
                    add_file = MIMEBase('application', 'octet-stream')
                    add_file.set_payload(f.read())
            encoders.encode_base64(add_file)
            add_file.add_header('Content-Disposition', 'attachment', filename = 'demo.txt')
            self.mail.attach(add_file)
    # 更改附件
    # 參數為 list
    def set_attach(self, file_list):
        self.attachment.extend(file_list)
    # 更改標題
    # 參數為 str
    def set_subject(self, subject):
        self.subject = subject
    # 更改信件內容
    # 參數為 str
    def set_contents(self, content):
        self.contents = content
    # 更改發送方的mail
    # 參數為 str, str
    def change_user(self, address, password):
        self.user.set_user(addressm, password)
        


# In[30]:


send_mail = send_Mail('address@gmail.com', 'password')
send_mail.set_subject('This is Notification')
send_mail.set_contents('Hello kitty')
send_mail.set_attach(['./text.txt',])
send_mail.send(['address@gmail.com'])

