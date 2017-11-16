import numpy as np
import matplotlib.pyplot as plt
import json


def get_asset_pair_name(asset1: str, asset2: str) -> str:
    return f'X{asset1}Z{asset2}'


holdings = dict()
try:
    file = open('../portfolio.json', 'r')
    holdings = dict(json.load(file))
    file.close()
except IOError:
    print('Cannot open file')

# get is from an exchange later
rates = {'XETHZEUR': 276.78,
         'XNEOZEUR': 24.9,
         'XLSKZEUR': 8.18,
         'XIOTZEUR': 0.66516,
         'XADAZEUR': 0.02269,
         'XOAXZEUR': 0.3042}

base_currency = 'EUR'
portfolio = {asset: count * rates[get_asset_pair_name(asset, base_currency)]
             for asset, count in holdings.items()}

total_value = sum(portfolio.values())
labels = portfolio.keys()
sizes = portfolio.values()

color1 = np.array([0.4, 1, 0.4])
color2 = np.array([0.4, 0.4, 1])
colors = [color1 * alpha + color2 * (1-alpha) for alpha in np.arange(len(sizes))/len(sizes)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes,
        colors=colors,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title(f'Portfolio {total_value:.2f}{base_currency}')
plt.show()
