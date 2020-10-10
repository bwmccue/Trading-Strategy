# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl 
import datetime



#------------------------------Setting Up--------------------------------
#person API key
quandl.ApiConfig.api_key = "RExs4Kvn4uMa4eXrpnhF"

#-----------------------Variable Setup--------------------------
#start time variable
start = datetime.datetime(2010,1,1)
#end time variable 
end = datetime.date(2018, 3, 27)

#SMA Variable 1
SMA1 = 50
#SMA Variable 2
SMA2 = 200
#Ticker Symbol
s = "AMD"

#stores ticker symbol data between the start and end date into the variable data
dataFromQuandl =  quandl.get("WIKI/" + s, start_date = start, end_date = end)

#stores data from variable "dataForQuandl" into a pandas DataFrame
df = pd.DataFrame(data = dataFromQuandl, columns = ["Date", "Close"])




#-----------------------------Moving Averages-------------------------
#By setting window = SMA, I can change SMA variable at the top to change 
#what SMA is being calculated
df["SMA 50"] = df.iloc[:,1].rolling(window=SMA1).mean()
#Second SMA meed to change the value of each line or else it will only print one line
df["SMA 200"] = df.iloc[:,2].rolling(window=SMA1).mean()






#---------------------------Printing Data and Creating plot--------------------
#Prints the value of "Close" from data at entry position 2 (Starts at 0, 1, 2...etc)
print(df["Close"][0])
#Can seach the list for individual dates
print(df["Close"]["2010-01-04"])
#Prints entire list
print(df)
#Creates a chart of the data from the list "df"
plt.figure(figsize=[15,10])
plt.grid(True)
#Plots closing data
plt.plot(df["Close"],label="data")
#Plots 50 SMA
plt.plot(df["SMA 50"],label="SMA Line 50")
#Plots 200 SMA
plt.plot(df["SMA 200"],label="SMA Line 200")


#------------------------------------NOTES----------------------------------------
#What to implement: 
    #MACD
    #Moving averages(20, 50, 200)
    #RSI
    #I can use closing price data to calculate moving averages
#RSI calculated using moving averages
#Look up how to build MACD


#Overall goal is to have trading strategy that goes through a series
#of conditions and give us ticker symbols that meet these conditions

#We will use Captial Asset Pricing Model to determine what ticker symbols
#will run our trading strategy on
    #
