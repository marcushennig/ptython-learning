import csv
import datetime
from typing import Dict, Any

import numpy as np
import matplotlib.pyplot as plt


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

time = np.array([k for k, v in thx_time_series.items()])
thx = np.array([v for k, v in thx_time_series.items()])

# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# ----------------------------------------------------------------------------------------------------------------------
# Figure 1
# ----------------------------------------------------------------------------------------------------------------------

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)


plt.plot(time, thx, color=[1, 0, 0], linewidth=2.5, linestyle="-")


plt.xlabel('time')
plt.ylabel('Number of daily transactions')
plt.show()