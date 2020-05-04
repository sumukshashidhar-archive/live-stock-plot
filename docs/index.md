# Live Stock Plots

This is a simple python package to retrieve and plot live stock data



# How to use this tool?

From the source folder, open up the yahoo_finance_fetch.py and pass the ticker as an argument. For example

`python3 src/retrieve/yahoo_finance_fetch.py --ticker AAPL --recall 300 --seconds 15`

The above line starts getting data for apple stock, and has data for 300 iterations, each iteration collected every 15 seconds. This translates to data for the last 1.5 hours 

**This must be run from the root directory, and not from the source directory**

To visualize the data that you get

`python3 src/plotting/live_plot.py --path ./data/AAPL_2020-05-03.csv`


> These are samples. Yours will be different, based on the data you wish to visualize.


Once you're done with your session, to remove the collected data, you can use the clean script

`python3 src/clean/clean_data.py`
