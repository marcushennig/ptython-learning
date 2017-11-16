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
ETHEUR = np.array([v.open for k, v in history.items()])


# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# ----------------------------------------------------------------------------------------------------------------------
# Figure 1
# ----------------------------------------------------------------------------------------------------------------------

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

plt.plot(T, ETHEUR, color='blue', linewidth=2.5, linestyle="-")

plt.xlabel('time')
plt.ylabel('ETH/EUR')
plt.show()

