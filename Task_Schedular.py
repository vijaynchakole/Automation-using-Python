# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:41:41 2020

@author: hp
"""

import schedule
import time 
import datetime


def fun_second():
    print("inside fun_second Current time is : ")
    print(datetime.datetime.now())
    print("Schedular executed after every 30 seconds \n")


def fun_minute():
    print("inside fun_minute Current time is : ")
    print(datetime.datetime.now())
    print("Schedular executed after Minute \n")
    

def fun_hour():
    print("inside fun_hour Current time is : ")
    print(datetime.datetime.now())
    print("Schedular executed after every hour \n")
    
def fun_day():
    print("inside fun_day current time is : ")
    print(datetime.datetime.now())
    print("Schedular fun_day executed after every sunday \n")
    

def fun_afternoon():
    print("inside fun_day current time is : ")
    print(datetime.datetime.now())
    print("Schedular fun_day executed after every afternoon at 12:00 PM \n")
   



def main():
    print("Python job Schedular ")
    
    print("inside Main Current time : ", datetime.datetime.now())
    
    schedule.every(30).seconds.do(fun_second)
    
    schedule.every(1).minutes.do(fun_minute)
    
    schedule.every().hour.do(fun_hour)
    
    schedule.every().sunday.do(fun_day)  
    
    schedule.every().saturday.at("16:30").do(fun_day)
    
    schedule.every().tuesday.at("17:15").do(fun_day)
    
    schedule.every().day.at("12:00").do(fun_afternoon)

    
    while True :
        schedule.run_pending()
        time.sleep(1)
        
    
if __name__ == "__main__":
    main()