# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 01:37:24 2020

@author: hp
"""

import requests
import bs4


def LinksDisplay(URL):
    
    res = requests.get(URL)
    
    res.text
    
    page_soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    links = page_soup.find_all('a', href = True)
    
    return links


def main():
    
    URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    
    ARR = LinksDisplay(URL)
    
    for element in ARR :
        if'#'not in element['href']:
          print(element['href'])
        
        
        
    
    

if __name__ == "__main__":
    main()