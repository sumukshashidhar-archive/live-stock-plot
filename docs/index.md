# Live Stock Plots

This is a simple python package to retrieve and plot live stock data



# How to use this tool?

From the source folder, open up the yahoo_finance_fetch.py and pass the ticker as an argument. For example

`python3 src/retrieve/yahoo_finance_fetch.py --ticker AAPL --recall 300 --seconds 15`

The above line starts getting data for apple stock, and has data for 300 iterations, each iteration collected every 15 seconds. This translates to data for the last 1.5 hours.

> Note: Yahoo finance query apis allow upto 2000 requests per hour only if I'm not mistaken. This translates to around 2 requests a seconds, which is generous. However, an increased number of requests may set off an abuse detection mechanism and leave you banned. Do so at your own risk.

**This must be run from the root directory, and not from the source directory**

To visualize the data that you get

`python3 src/plotting/live_plot.py --path ./data/AAPL_2020-05-03.csv --interval 100`

The above line starts a live_plot for the given data, which updates at a 100ms interval

> These are samples. Yours will be different, based on the data you wish to visualize.


Once you're done with your session, to remove the collected data, you can use the clean script

`python3 src/clean/clean_data.py`


# Power of Source Modification

Modifying the source can give you some extra power

## Realtime Data

### How to enable realtime data

1. For actual realtime data, remove the time.sleep() statement from the `periodic_fetch_loop`.
2. Set the interval for the live_plot.py file to be 1ms

**To further improve speeds, comment out the call to the clean function**

### Factors affecting accuracy
(This data will be as close to realtime as possible, however, some factors affect the accuracy of the data)

**Factors dependent on you**
1. Network speed
2. IO speed of drives
3. History length

**Factors that cannot be controlled**
1. Yahoo Server Speeds
2. Python GIL
3. Code Inefficiencies
