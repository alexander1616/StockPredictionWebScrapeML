import re
import json
from io import StringIO
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

###
### Load symbol data info from page "quote-header-info"
###
def soupGetSymbolInfo(s, data = None):
    if data is None:
        data = {}
    symbol_hdr_info = s.find("div", {"id":"quote-header-info"} )
    if symbol_hdr_info is None:
            return None
    symbol_name = symbol_hdr_info.find('fin-streamer', {'data-field':'marketState'})
    data['DATA_SYMBOL'] = symbol_name['data-symbol']
    symbol_time = symbol_hdr_info.find('div', {'id':'quote-market-notice'})
    #print(symbol_time)
    data['DATA_TIME'] = symbol_time.text
    return data

###
### Process the left and right table from quote page
###
def soupFindTable(s_table, data=None):
    if data is None:
        data = {}
    tbody = s_table.find('tbody')
    rows = tbody.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        data[cols[0].text] = cols[1].text
    return data

###
### extract basic stock infomation from yahoo finance web site.
### given a stock
### return the basic finanical info in dictionary form.
###
def getStockInfo(stock):
    url_summary = 'https://finance.yahoo.com/quote/{0}?p={0}'
    ### hack the request to fool yahoo finance
    web_header={'Connection': 'keep-alive',
            'Expires': '-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
           }
    response = requests.get(url_summary.format(stock), headers=web_header)
    soup = BeautifulSoup(response.text, 'html.parser')

    ### setup return dict for symbol
    symbol_info = {}
    if soupGetSymbolInfo(soup, symbol_info) is None:
        print("MISSING SYMBOL {}".format(stock))
        return None
    if stock != symbol_info['DATA_SYMBOL']:
        print("SYMBOL {} != DATA_SYMBOL {}".format(stock, symbol_info['DATA_SYMBOL']) )
        print(symbol_info)
        return None

    script_data_left = soup.find("div", {"data-test":"left-summary-table"} )
    script_data_right = soup.find("div", {"data-test":"right-summary-table"} )

    soupFindTable(script_data_left, symbol_info)
    soupFindTable(script_data_right, symbol_info)

    return symbol_info

# df = pd.DataFrame ( [ getStockInfo(symbol) for symbol in "ENPH IBM RY".split() ] )
# getStockInfo('XYZ')
