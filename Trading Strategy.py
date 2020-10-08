# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import pandas as pd
import quandl 
import datetime

#person API key
quandl.ApiConfig.api_key = "RExs4Kvn4uMa4eXrpnhF"

#start time variable
start = datetime.datetime(2000,1,1)
#end time variable 
end = datetime.date(2018, 3, 27)

#Ticker Symbol
s = "AAPL"

#stores ticker symbol data between the start and end date into the variable data
dataFromQuandl =  quandl.get("WIKI/" + s, start_date = start, end_date = end)

#prints data to console
type(dataFromQuandl)

#Prints the value of "Close" from data at entry position 2 (Starts at 0, 1, 2...etc)
print(dataFromQuandl["Close"][1])

#stores data from variable "dataForQuandl" into a pandas DataFrame
df = pd.DataFrame(data = dataFromQuandl, columns = ["Close"])
print(df)

#Instead of indexing 0-x you can search for specific dates
df = df.set_index('dates')





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
