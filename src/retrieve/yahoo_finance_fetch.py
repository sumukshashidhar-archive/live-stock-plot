# Author: Sumuk Shashidhar
# License: BSD
# You must credit the author / link the source if you decide to use this

## Imports

import urllib.request
import json
from datetime import date
import time
import argparse



def clean(history, filename):
	"""
	This function takes in the max allowed history and deletes old lines

	Arguments:
	history {int} -- The max allowed lines
	filename {String} -- The path to the file you need to clean
	"""

	with open(filename, "r") as fclean:
		lines = fclean.readlines()

	if len(lines) >= history:
		with open(filename, "w") as fcleaned:
			for i in range(1, len(lines)):
				fcleaned.write(lines[i])


## this url puts the ticker variable into the yahoo query1 api
def stdout(price_data, market_time,stock_name):
	"""
	This function takes in the listed arguments and outputs to a file in the data directory

	Arguments:
	price_data {float} -- The current regular market price of the data
	market_time {int} -- Unix time of retrieval of data
	stock_name {String} -- The ticker of the stock to identify the created file
	"""
	try:
		f = open(str("./data/"+stock_name+'_'+str(date.today())+ ".csv"), 'a')
	except FileNotFoundError:
		try:
			f = open(str("./data/"+stock_name+'_'+str(date.today())+ ".csv"), 'w')
		except:
			print("You are running the file directly from the source directory. \n This is not supported at the time \n  Please run it from the root directory of the repo")
	finally:
		clean(history, str("./data/"+stock_name+'_'+str(date.today())+".csv"))
		f.write(str(str(market_time) + ',' + str(price_data)))
		f.write('\n')
		f.close()



def data_parse(new_data):
    """
    This function parses the raw html data

    Arguments:
        new_data {HTTPResponse} -- The raw http response from the webpage
    """
    string = new_data.read().decode('utf-8')
    data_parsed = json.loads(string)
    data_parsed = data_parsed["quoteResponse"]["result"][0]
    # print(json.dumps(data_parsed, indent=4)) ## for debugging purposes
    stdout(data_parsed["regularMarketPrice"], data_parsed["regularMarketTime"], ticker)

def get_new_data():
    """
    Gets new data from the yahoo finance api
    """
    new_data = urllib.request.urlopen(url)
    data_parse(new_data)


def periodic_fetch_loop():
    """
    Just to keep collecting data
    """
    while(True):
        ## try fetching every 10 seconds
        get_new_data()
        time.sleep(9)


parser = argparse.ArgumentParser()

parser.add_argument("-r", "--recall", help="Set the max history for the plot. DEFAULT=200")
parser.add_argument("-t", "--ticker", help="Add the ticker")
parser.add_argument("-s", "--seconds", help="The number of seconds between each fetch. DEFAULT=10")
args = parser.parse_args()


history = int(args.recall) if args.recall!=None else 200
seconds = int(args.seconds) if args.seconds!=None else 10

if args.ticker == None:
	print("Please pass in the ticker argument for this to work")
	exit()
else:
	ticker = args.ticker
	url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="+ ticker + "&range=1d&interval=5m&indicators=close&includeTimestamps=false&includePrePost=false&corsDomain=finance.yahoo.com&.tsrc=finance"
	print("\n\n\n\n")
	print("Pass this as an argument to the plotting module for it to start up \n \n"+ "./data/"+ticker+'_'+str(date.today())+ ".csv" + "\n\n")
	print("Killing this terminal stops data retrieval. Do so at your own risk")
	periodic_fetch_loop()
