# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:30:51 2020

@author: hp

google account setting -> Securty -> Less secure app access turn it = ON
"""

from sys import *
import time
import smtplib
from urllib.request import urlopen


def is_connected():
    
    try:
        urlopen("https://www.google.com/", timeout = 2)
        return True
    except URLError as err:
        return False
    

def MailSender(gmail_user, gmail_password):
    
    sendfrom = gmail_user
   # to = ['vijaynarsingchakole10@gmail.com']
    to = sendfrom 
    
    email_text = "Jay ShreeRam"
    
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        #server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sendfrom,to, email_text,)
        server.close()
        print("Mail send successfully")
    except Exception as E:
        print("Unable to send Mail ", E)
    
    
    
    
def main():
    print("inside main Mail_Sender")
    print("Application Name "+ argv[0])
    
    
    try:
        
        user_name = "vijaychakole23@gmail.com"
        password = "BigRevenge@2020"
        
        if is_connected():
            
            print("connection Successfully done")
            
            
            start_time = time.time()
            MailSender(user_name, password)
            end_time = time.time()
            
            print(f"time taken for mail send is {end_time - start_time} ")
        
                
        else:
            print("there is no connection")
        
    except Exception as E:
        print("ERROR : invalid input ", E)
        
        
        
        
if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        