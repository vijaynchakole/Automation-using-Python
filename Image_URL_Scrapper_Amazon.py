# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:31:02 2020

@author: hp
"""

import os
import bs4
from sys import *
import requests
from urllib.request import urlopen




def ImageURLScrapper(url):
    
    connection = urlopen(url)
    
    raw_html = connection.read()
    
    page_soup = bs4.BeautifulSoup(raw_html, "html.parser")
    
    container = page_soup.findAll("div", {"class" : "item-container"})
    
    return container



def main():
    print("inside main")
    
    try:
        url = "https://www.newegg.com/"
        
        listout = ImageURLScrapper(url)
        
        for element in listout:
            
            print(element.img['src'])

    
    except Exception as E:
        print(E)



if __name__ == "__main__":
    main()