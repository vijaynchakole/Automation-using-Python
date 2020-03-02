# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 01:18:32 2020

@author: hp

Automation script which fetch title and
content headers of wikipedia page using Beautiful Soup.

"""

import bs4
import requests


res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

type(res)

res.text

page_soup = bs4.BeautifulSoup(res.text, 'lxml')

type(page_soup)

title = page_soup.select('title')

type(title)

print(title[0].getText())

arr = page_soup.select('.mw-headline')  # 'mw-headline' is class name in web text
type(arr)


for element in arr:
    print(element.text)


