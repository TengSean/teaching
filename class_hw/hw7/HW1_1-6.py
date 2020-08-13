#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:18:55 2020

@author: amanda
"""
import pickle

class BankAccount:
    

    
    def __init__(self,name,phone,usemoney,spendmoney):
        self.name = name
        self.phone = phone
        self.usemoney = usemoney
        self.spendmoney = spendmoney
    
    def  __str__(self):
        return "請輸入姓名,請輸入聯絡電話,請輸入信用額度,請輸入新增消費金額"
    
    def check_expense(self,money):
        if self.usemoney > self.spendmoney + money :
           self.spendmoney = self.spendmoney + money
        else : 
           print("超過信用額度")
    
    def check_balance(self):
        print(self.usemoney - self.spendmoney)
        
x = input("請輸入姓名: , 請輸入聯絡電話: , 請輸入信用額度: ")
if x == "a" :      
    name = input("name: ")        
    phone = input("phone: ")
    usemoney = int(input("usemoney: "))
    spendmoney = int(input("spendmoney: "))
    bankaccount = BankAccount(name,phone,usemoney,spendmoney)
    filename = name + ".pkl"
    
    with open(filename,"wb") as f :
    
        pickle.dump(bankaccount,f)
    del bankaccount
    
elif x == "b" :
    name = input ("name: ")
    money = int(input ("spendmoney: "))
    filename = name + ".pkl"
    
    with open(filename,"rb") as f :
        y = pickle.load(f)
        y.check_expense(money)
    
    with open(filename,"wb") as f :
        pickle.dump(y,f)
        
elif x == "c" :
    name = input("name: ")
    filename = name + ".pkl"
    with open(filename,"rb") as f :
      y = pickle.load(f)
      y.check_balance()
    
        
        





