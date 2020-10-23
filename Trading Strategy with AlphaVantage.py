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
import time

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


#------------------------------Setting Up--------------------------------
#person API key
quandl.ApiConfig.api_key = "RExs4Kvn4uMa4eXrpnhF"

#Alpha Vantage Key
alpha_vantage_key = 'SGO5M0QZ92JS8IRK'
alpha_vantage_key2 = 'CDTFKPQFW0Y9OZ5T'
alpha_vantage_key3 = 'CLXZ3UPUE8STZJOP'

#What stock we want to look at
tickerSymbol = 'pton'

#The interval the data is collected and sent to us
#For time_series data we can do "1min", "5min", "15min", "30min", "60min"
#If we want daily data, change function to = TIME_SERIES_DAILY
intervalLength = '30min'
smallSMATime = 50
largeSMATime = 200

#----------------------------------Time Series Data----------------------------------------
#These need to be ran initally to generate an excel file of the most current stock data
#Unless you are looking at a diffrent stock or time interval, you only need to run these once per day for testing purposes
ts = TimeSeries(key = alpha_vantage_key2, output_format='pandas')
dataDaily, meta_data = ts.get_daily_adjusted(symbol = tickerSymbol)
dataIntraDay, meta_data = ts.get_intraday(symbol = tickerSymbol, interval = intervalLength)

#-------------------------------Technical Indicators--------------------------------------

ti = TechIndicators(key = alpha_vantage_key3, output_format='pandas')

dataMACD, meta_data = ti.get_macd(symbol = tickerSymbol, interval = 'daily', fastperiod = 12, slowperiod = 26, signalperiod = 9)

dataSmallSMA, meta_data = ti.get_sma(symbol = tickerSymbol, interval = 'daily', time_period = smallSMATime)
dataLargeSMA, meta_data = ti.get_sma(symbol = tickerSymbol, interval = 'daily', time_period = largeSMATime)

#dataRSI, meta_data = ti.get_rsi(symbol = tickerSymbol, interval = 'daily', time_period = 200, series_type = 'close')


#----------------------------------Plotting Data---------------------------------------
dataMACD.plot()
plt.title("MACD for MSFT")
plt.grid(True)
plt.show()

#dataSmallSMA.plot()
#dataLargeSMA.plot()
#plt.title('SMA')
#plt.grid(True)
#plt.show()

#dataRSI.plot()
#plt.title('RSI')
#plt.grid(True)
#plt.show()


#---------------------------------Building Excel Files---------------------------------------
#saving daily time series data to a pandas list
dailyData = pd.DataFrame(dataDaily)
dailyData.to_csv('dailyData of ' + tickerSymbol + '.csv')

#saving intra daily time series data to a pandas list
#intraDailyData = pd.DataFrame(dataIntraDay)
#intraDailyData.to_csv('intraDailyData of ' + tickerSymbol + '.csv')

#saving macd to pandas list
#macdData = pd.DataFrame(dataMACD)
#macdData.to_csv('MACD of ' + tickerSymbol + '.csv')

#saving small SMA to pandas list
smallSMAData = pd.DataFrame(dataSmallSMA)
smallSMAData.to_csv(str(smallSMATime) + ' SMA of ' + tickerSymbol + '.csv')

#saving large SMA to pandas list
largeSMAData = pd.DataFrame(dataLargeSMA)
largeSMAData.to_csv(str(largeSMATime) +' SMA of ' + tickerSymbol + '.csv')

#saving rsi to pandas liist
#rsiData = pd.DataFram(dataRSI)
#rsiData.to_csv('RSI of ' + tickerSymbol + '.csv')


#------------------------------------Conditional Statements------------------------------------

i=1
print(smallSMAData['2019-12-10']) 
a=1
smaCount = 0
for i in range(len(smallSMAData)):
    
    if smallSMAData[i] > largeSMAData[i]:
        smaCount = smaCount + 1
        i+1
    
    if smaCount == 3:
        print("3 day positiveSMA crossover value" + str(dataDaily[i]) + str(dataDaily[i-1]) + str(dataDaily[i-2]))
              
    



#------------------------------------NOTES----------------------------------------
# 1st) MACD Divergence (increasing MACD & decreasing price)
# 2nd) 50SMA > 200SMA
# 3rd) RSI < 70
