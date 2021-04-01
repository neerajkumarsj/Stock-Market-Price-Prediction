'''
Created on Sun Jun  7 16:39:38 2020

@author: Neeraj Kumar sj

Description : This file updates time and date for the graph and while recording 
              the stock price to the 'stock.csv' file.
              This File is to be excuted Second.
              Before this execute 'prices1.py'
'''

#Including the necassary modules for date and time
import pandas as pd
from datetime import datetime
from datetime import timedelta
import time
# A class called time is created
class stock():
    #This function is used to call this class to a different file
    def __init__(self):
        pass
    #This function is used for updating date and time details simultaneously
    def graphtime(end):
        i = True
        c = time.localtime(time.time())#Here we call the present time in the form af list
        #d is used to store date and time in the file
        d = str(str(c[2])+'/'+str(c[1])+'/'+str(c[0])+'|'+str(c[3])+'-'+str(c[4])+'-'+str(c[5]))
        #t is used to display time in the graph
        t = str(str(c[3])+':'+str(c[4])+':'+str(c[5]))
        #s is used to stop the execution when the maket closes.
        s = str(str(c[3])+':'+str(c[4]))
        if s != end:
            #print(str(c[3])+':'+str(c[4])+':'+str(c[5]))
            time.sleep(1)
            i = True
            
        elif s == end:
            print('Market Has Closed!!')
            i = False
            time.sleep(65)
            exit(0)
        return t,d,s
        
