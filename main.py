# from Kraken.kraken_api import KrakenAPI
# kraken = KrakenAPI()
# data = kraken.get_ohlc_data_for_asset('XETHZEUR', 1)

import numpy as np
import matplotlib.pyplot as plt

# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# ----------------------------------------------------------------------------------------------------------------------
# Figure 1
# ----------------------------------------------------------------------------------------------------------------------

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S = np.sin(X)
C = np.cos(X)

plt.plot(X, C, color='blue', linewidth=2.5, linestyle="-")
plt.plot(X, S, color='green', linewidth=1.0, linestyle="-")

plt.xlim(-4.0, 4.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.xlabel('X')

plt.ylim(-1.0, 1.0)
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
plt.ylabel('Y')

# Save figure using 72 dots per inch
# plt.savefig("exercice_2.png", dpi=72)

# Show result on screen
plt.show()
