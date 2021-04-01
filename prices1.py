# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:32:47 2020

@author: Neeraj Kumar S J
"""
"""
Description : This file updates the stock prices directly from the website 'yahoofinace.com' for the graph 
              and while recording to the stock price to the 'stock.csv' file.
              This File is to be excuted first.
              Before this execute stoctime.py
              
Installation Code for Included Modules:
    bs4 : conda - 'conda install -c anaconda beautifulsoup4'
          pip - 'pip install bs4'
    requests : conda- 'conda install -c anaconda requests'
               pip = 'pip install requests'
"""
#Including the necassary modules for webscarping
import bs4
import requests
from bs4 import BeautifulSoup
import time

#A class called prices is created
class prices():
    #This fucntion enables us to call this class to diffren file.
    def __init__(self, Price):
        self.stprice = Price
    #This function extracts the price directly from the web for now we are using Facebook's Stock prices
    def parsePrice():
        r = requests.get('https://in.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch')#Here we use the webpage url
        soup = bs4.BeautifulSoup(r.text,"lxml")#here we extract webapge code
        price = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text#Here we find and extract the price of the fb stock price.
        return price