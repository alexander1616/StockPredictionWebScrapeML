###
###
### Provides two functions to extract stock data into a dataframe using yahoo finance
###
### Copyright 2023 - Alex Chan
###
### 7/18/2023 - Created
###
###

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta

###
### get_stock_data - extracts stock data
### parameters - symbol, numDays
###
def get_stock_data(symbol, numDays = 5000):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    end_date = d1
    d2 = date.today() - timedelta(days = numDays)
    d2 = d2.strftime("%Y-%m-%d")
    start_date = d2
    data = yf.download(symbol, 
                      start=start_date, 
                      end=end_date, 
                      progress=False)

    data["Date"] = data.index
    data = data[["Date", "Open", "High", "Low", "Close",
             "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)
    data.tail()
    return data

###
### get_stock_data2 - extracts stock data
### parameters - symbol, numDays
###
def get_stock_data2(symbol, numDays= "5000"):
    stock = yf.Ticker(symbol)
    data = stock.history(period = numDays)
    data = data[["Open", "High", "Low", "Close",
                "Volume"]]
    return data
