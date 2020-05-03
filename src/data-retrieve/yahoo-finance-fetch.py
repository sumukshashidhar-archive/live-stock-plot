# Author: Sumuk Shashidhar
# License: BSD
# You must credit the author / link the source if you decide to use this

## Imports

import urllib.request
import json
from datetime import date

ticker = 'AAPL' ## no ticker
# ticker_get() #disable this if you pre specify the ticker directly in the file

## this url puts the ticker variable into the yahoo query1 api
url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="+ ticker + "&range=1d&interval=5m&indicators=close&includeTimestamps=false&includePrePost=false&corsDomain=finance.yahoo.com&.tsrc=finance"

# print(url)

def stdout(data, stock_name):
    try:
        f = open("./../../data/"+stock_name+'_'+str(date.today())+ ".csv", 'a')
    except FileNotFoundError:
        f = open("./../../data/"+stock_name+'_'+str(date.today())+ ".csv", 'w')
    finally:
        f.write(str(data))
        f.write('\n')
        f.close()



def data_parse(new_data):
    string = new_data.read().decode('utf-8')
    data_parsed = json.loads(string)
    data_parsed = data_parsed["quoteResponse"]
    data_parsed = data_parsed["result"]
    data_parsed = data_parsed[0]
    # print(data_parsed)
    print(json.dumps(data_parsed, indent=4))
    # print(data_parsed.keys())s
    data = data_parsed["regularMarketPrice"]
    stdout(data, ticker)

def get_new_data():
    new_data = urllib.request.urlopen(url)
    data_parse(new_data)



def periodic_fetch_loop():
    pass


get_new_data()
