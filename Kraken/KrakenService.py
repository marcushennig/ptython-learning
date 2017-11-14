import urllib.request
import json
from typing import Dict

from Kraken.AssetInfo import AssetInfo


class KrakenService:

    def __init__(self):
        self.url = ''

    @staticmethod
    def get_asset_info(asset: str) -> AssetInfo:
        """Get information for a given asset from kraken"""

        values = {'asset': asset}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')  # data should be bytes

        with urllib.request.urlopen('https://api.kraken.com/0/public/Assets', data) as response:
            data = json.load(response)
            result = dict(data['result'])

            if asset in result:
                info = result[asset]
                return AssetInfo(alternate_name=info['altname'],
                                 asset_class=info['aclass'],
                                 decimals=info['decimals'],
                                 display_decimals=info['display_decimals'])

        return AssetInfo.empty()


    def get_rate(self, rate: str) -> float:
        """Return the current exchange rate of ETH-EUR"""
        if rate == 'ETHEUR':
            return 234.3
        else:
            return 0.0
