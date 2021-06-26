# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:01:54 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
page= requests.get("https://www.keralapropertyfinder.com/Search/rn/1/0/0/277/0/kannur", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
soup = BeautifulSoup(page.content, 'html5lib')
table = soup.find('div', attrs = {'class':'row portfolio-items'}) 
cards=table.findAll('div', attrs = {'class':'project-single'})

quotes=[]

for cards in cards:
    price=cards.find('div',attrs={'class':'price-properties'})
    types=cards.find('div',attrs={'class':'homes-price'})
    
   
    quote = {}
    quote['theme'] = cards.h3.text
    quote['ROOMS']=cards.ul.span.text
    quote['Home']=cards.p.span.text
    quote['price']=price.h3.text.strip()
    quote['type']=types.text.strip()
   
    
   
    quotes.append(quote)


import pandas as pd
dataaas=pd.DataFrame(quotes)

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["projectbase"]
mycol = mydb["kannur"]

mycol.insert_many(quotes)