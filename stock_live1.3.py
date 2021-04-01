# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:21:34 2020

@author: Neeraj Kumar S J
"""
"""
Description - This code, creates the live stock price graph, i.e. 
updated every second, just like the live stock market price graph
Steps for Execution:
    1. Run prices1.py
    2. Run stoctime.py
    3. Run stock_live.py
    4. Input - Time when stock market closes is to be given in 24 hrs format
                with never type '0' for single digit values, 
                For example: 19:05- Wrong
                             19:5-Right,
               Else this graph runs infnitely, and when the market closes the 
               graph goes constant with
               the closing price.
    5. Output - 1. Live updating Stock Price Graoh
                2. A .csv file (stock.csv) which records the prices that is 
                   being shown in the graph with its respective time and date.
    6. End - Just Close the graph if clsong time is not given.
             Else when the time is up it displays "Market has Closed!!"
             and waits for 60 seconds and terminates the code.
"""
#Included all the modules and classes which was created.
import pandas as pd
import prices1 as pr
import stimes
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#Outline of graph is created
plt.style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig.show()
#initializations of all the variables
x_axis = []
y_axis = []
z = []#It is used to update and store date and time in the file
c = []#It is used to satisfy the if condition 
end = str(input('Entert the market closing time (in hh:mm. and hh = are in 24 hrs and if it is a single digit do not add "0" :-'))

if end == '':
    end = str('16:0')
        
    
def animate(i):
    if end != stimes.stock.graphtime(end)[2]:
        y_axis.append(float(pr.prices.parsePrice()))#Prices are extaracted and stored.
    else:
        print('Market Has Closed!!!')
        time.sleep(65)
        return(0)
    x_axis.append(stimes.stock.graphtime(end)[0])#respective time are updated and stored
    z.append(stimes.stock.graphtime(end)[1])#respective time are updated and stored
    c.append(stimes.stock.graphtime(end)[2])#respective time are updated and checked with if statement
    df = pd.DataFrame(data={"Date":z , "close": y_axis})
    df.to_csv("stock.csv", sep=',',index=False)#the data is written to the .csv file
    #Orientation of the graph is detailed here
    plt.cla()
    plt.xticks(rotation=90)
    size=10
    params = {'legend.fontsize': 'large',
              'figure.figsize': (5,5),
              'axes.labelsize': size,
              'axes.titlesize': size,
              'xtick.labelsize': size*0.75,
              'ytick.labelsize': size*0.75,
              'axes.titlepad': 25}
    plt.rcParams.update(params)
    plt.title('Apple Closing Price History')
    plt.xlabel('Time')
    plt.ylabel('Apple Stock prices')
    ax.plot(x_axis,y_axis,color='blue', linewidth=1)
    plt.tight_layout()
    plt.savefig("sample.jpg")
    
#Live updating graph is created here
livegraph = FuncAnimation(plt.gcf(), animate, interval = 1000)
print('loading...')

#The graph is shown here
plt.show()
