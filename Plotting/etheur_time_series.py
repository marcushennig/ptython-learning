from Kraken.kraken_api import KrakenAPI

import datetime
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------
# Load transaction history for ethereum
# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
# Download OHLC data for asset pair ETH/EUR
# ----------------------------------------------------------------------------------------------------------------------

kraken = KrakenAPI()
history = kraken.get_ohlc_data_for_asset('XETHZEUR', 240)
kraken.close()

# ----------------------------------------------------------------------------------------------------------------------
# get data into numpy array
# ----------------------------------------------------------------------------------------------------------------------

time = np.array([datetime.datetime.utcfromtimestamp(t) for t, value in history.items()])

ETHEUR_low = np.array([v.low for k, v in history.items()])
ETHEUR_average = np.array([v.vwap for k, v in history.items()])
ETHEUR_high = np.array([v.high for k, v in history.items()])


# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# ----------------------------------------------------------------------------------------------------------------------
# Figure 1
# ----------------------------------------------------------------------------------------------------------------------

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)


domain = ETHEUR_average > 0
plt.plot(time[domain], ETHEUR_average[domain], color=[1, 0, 0], linewidth=2.5, linestyle="-")


plt.xlabel('time')
plt.ylabel('ETH/EUR')
plt.show()

