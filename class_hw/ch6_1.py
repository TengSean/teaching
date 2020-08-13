#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:51:23 2020

@author: amanda
"""

import re 
Account = input('Enter account\n')
password = input('Enter password\n')
if re.match(r"[a-zA-Z0-9.]*$",Account) and re.match(r"(?=.*[^a-zA-Z0-9\d]).{8,}$",password):
    print("通過測試")
else:
    if not re.match(r"[a-zA-Z0-9.]*$",Account) and not re.match(r"(?=.*[^a-zA-Z0-9\d]).{8,}$",password):
        print ("帳號格式錯誤 密碼格式錯誤")
    elif not re.match(r"[a-zA-Z0-9.]*$",Account):
        print("帳號格式錯誤")
    else:
        print("密碼格式錯誤")