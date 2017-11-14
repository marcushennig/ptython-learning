import urllib.request
import json
from Kraken.AssetInfo import AssetInfo
from typing import Dict

# Check https://github.com/veox/python3-krakenex/tree/master/examples


class KrakenAPI:
    """ Check https://www.kraken.com/help/api#public-market-data for the API"""

    def __init__(self):
        self.uri = 'https://api.kraken.com'
        self.api_version  = 0

    def get_tradable_asset_pair(self, asset_pair: str):
        pass

    def _query(self, url_path: str, data: Dict[str, str], headers=None):
        """ Low-level query handling.
        .. note::
           Use :py:meth:`query_private` or :py:meth:`query_public`
           unless you have a good reason not to.
        :param urlpath: API URL path sans host
        :type urlpath: str
        :param data: API request parameters
        :type data: dict
        :param headers: (optional) HTTPS headers
        :type headers: dict
        :returns: :py:meth:`requests.Response.json`-deserialised Python object
        :raises: :py:exc:`requests.HTTPError`: if response status not successful
        """
        if data is None:
            data = {}
        if headers is None:
            headers = {}

        url = self.uri + url_path

        self.response = self.session.post(url, data=data, headers=headers)

        if self.response.status_code not in (200, 201, 202):
            self.response.raise_for_status()

        return self.response.json()

    def query_public(self, method: str, data: Dict[str, str]=None):
        """ Performs an API query that does not require a valid key/secret pair.
        :param method: API method name
        :type method: str
        :param data: (optional) API request parameters
        :type data: dict
        :returns: :py:meth:`requests.Response.json`-deserialised Python object
        """
        if data is None:
            data = {}

        url_path = f'/{self.api_version}/public/{method}'

        return self._query(url_path, data)

    def get_asset_info(self, asset: str) -> AssetInfo:
        """Get information for a given crypto currency from kraken"""

        values = {'asset': asset}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')  # data should be bytes

        with urllib.request.urlopen(f'{self.uri}/{self.api_version }/public/Assets', data) as response:
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
