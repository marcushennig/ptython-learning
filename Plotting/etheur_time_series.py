from Kraken.kraken_api import KrakenAPI
from typing import Dict, Any

import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime


# ----------------------------------------------------------------------------------------------------------------------
#
# https://www.forbes.com/sites/wwoo/2017/09/29/is-bitcoin-in-a-bubble-check-the-nvt-ratio/#60c0324c6a23
#
# Load transaction history for ethereum
# ----------------------------------------------------------------------------------------------------------------------

def load_thx_file(path: str) -> Dict[Any, int]:

    thx_time_series = {}
    with open('ethereum-TxGrowth.csv') as tx_file:

        reader = csv.reader(tx_file, delimiter=',')
        # skip headers
        next(reader, None)

        for row in reader:

            unixTimeStamp = int(row[1])
            t = datetime.datetime.utcfromtimestamp(unixTimeStamp)
            numberOfThx = int(row[2])

            thx_time_series.update({t: numberOfThx})

    return thx_time_series

thx_time_series = load_thx_file('ethereum-TxGrowth.csv')

thx_time = np.array([k for k, v in thx_time_series.items()])
thx = np.array([v/1000 for k, v in thx_time_series.items()])


# ----------------------------------------------------------------------------------------------------------------------
# Download OHLC data for asset pair ETH/EUR
# ----------------------------------------------------------------------------------------------------------------------

kraken = KrakenAPI()
history = kraken.get_ohlc_data_for_asset('XETHZEUR', 10080)
kraken.close()

# ----------------------------------------------------------------------------------------------------------------------
# get data into numpy array
# ----------------------------------------------------------------------------------------------------------------------

t = np.array([datetime.datetime.utcfromtimestamp(t) for t, value in history.items()])
p = np.array([v.vwap for k, v in history.items()])
price_time = t[p > 0]
price = p[p > 0]


# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# ----------------------------------------------------------------------------------------------------------------------
# Figure 1
# ----------------------------------------------------------------------------------------------------------------------

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)


plt.plot(price_time, price, color=[1, 0, 0], linewidth=2.5, linestyle="-")
plt.plot(thx_time, thx, color=[0, 0, 1], linewidth=2.5, linestyle="-")

plt.xlabel('time')
plt.ylabel('ETH/EUR')
plt.show()

