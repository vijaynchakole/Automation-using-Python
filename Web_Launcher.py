# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:20:17 2020

@author: hp
"""

from urllib.request import urlopen
import re
import webbrowser
import os
# from argv commandline input
from sys import *



os.chdir("C:/Users/hp/PycharmProjects/Automation")

def is_connected():
    
    try:
        urlopen("https://www.google.com/" , timeout = 2)
        
        return True
    except URLError as err:
        print("Unable to connect ", err)
        return False
    
    
def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url


def WebLauncher(path):
    with open(path) as fd:
        for line in fd:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str, new = 2)
            
    
        
def main():

    connect = is_connected()
    if connect :
        try:
            print(argv[1])
            print("inside try block")
            WebLauncher(argv[1])
            #WebLauncher("WebList.txt")
        except Exception as E:
            print("Unable to open URL")
            
            
if __name__ == "__main__":
    main()

    