from Kraken.kraken_api import KrakenAPI
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------
# Download OHLC data for asset pair ETH/EUR
# ----------------------------------------------------------------------------------------------------------------------

kraken = KrakenAPI()
history = kraken.get_ohlc_data_for_asset('XETHZEUR', 1)
kraken.close()

# ----------------------------------------------------------------------------------------------------------------------
# get data into numpy array
# ----------------------------------------------------------------------------------------------------------------------

T = np.array([k for k, v in history.items()])
ETHEUR_low = np.array([v.low for k, v in history.items()])
ETHEUR_high = np.array([v.high for k, v in history.items()])


# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# ----------------------------------------------------------------------------------------------------------------------
# Figure 1
# ----------------------------------------------------------------------------------------------------------------------

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

plt.plot(T, ETHEUR_low, color=[0, 0, 1], linewidth=2.5, linestyle="-")
plt.plot(T, ETHEUR_high, color=[1, 0, 0], linewidth=2.5, linestyle="-")

plt.xlabel('time')
plt.ylabel('ETH/EUR')
plt.show()

