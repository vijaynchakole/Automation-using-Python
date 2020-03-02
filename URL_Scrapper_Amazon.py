# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:59:08 2020

@author: hp
"""

import os
from sys import *
import bs4
from urllib.request import urlopen
import requests



def URLScrapper(url):
    connection = urlopen(url)
    
    raw_html = connection.read()
    
    connection.close()
    
    page_soup = bs4.BeautifulSoup(raw_html,"html.parser")
    
    container = page_soup.findAll("a",{"class" : "a-link-normal a-text-normal"})    
    
    return container



def main():
    print("inside main MyURLScrappingAmazon")

    try:
        url = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2"
        listout = URLScrapper(url)

        print("URL from website is ")

        for elements in listout:
            fd = open("scrappedWeblist.txt","a")
            fd.write(elements['href'])
            fd.write("\n")
            print(elements['href'])
           # print(elements['class'])
    except Exception as E:
        print("Error : Invalid Input",E)




if __name__ == "__main__":
    main()
    





