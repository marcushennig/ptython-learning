import requests
from typing import Dict, List

from Kraken.asset_info import AssetInfo
from Kraken.ohlc_data import OHLCData
from . import version


# Check https://github.com/veox/python3-krakenex/tree/master/examples
class KrakenAPI:
    """ Maintains a single session between this machine and Kraken.
        Specifying a key/secret pair is optional. If not specified, private
        queries will not be possible.
        The :py:attr:`session` attribute is a :py:class:`requests.Session`
        object. Customise networking options by manipulating it.
        Query responses, as received by :py:mod:`requests`, are retained
        as attribute :py:attr:`response` of this object. It is overwritten
        on each query.
        .. note::
           No query rate limiting is performed.
        """

    def __init__(self, key='', secret=''):
        """ Create an object with authentication information.
        :param key: (optional) key identifier for queries to the API
        :type key: str
        :param secret: (optional) actual private key used to sign messages
        :type secret: str
        :returns: None
        """
        self.key = key
        self.secret = secret
        self.uri = 'https://api.kraken.com'
        self.api_version = '0'
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'krakenex/' + version.__version__ + ' (+' + version.__url__ + ')'})
        self.response = None

        return

    def close(self) -> None:
        """ Close this session.
        :returns: None
        """
        self.session.close()
        return

    def load_key(self, path: str) -> None:
        """ Load key and secret from file.
        Expected file format is key and secret on separate lines.
        :param path: path to key file
        :type path: str
        :returns: None
        """
        with open(path, 'r') as file:
            self.key = file.readline().strip()
            self.secret = file.readline().strip()
        return

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

    def query_public(self, method: str, data: Dict[str, str] = None):
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
        response = self.query_public('Assets', values)

        if asset in response:
            info = response[asset]
            return AssetInfo(alternate_name=info['altname'],
                             asset_class=info['aclass'],
                             decimals=info['decimals'],
                             display_decimals=info['display_decimals'])

        return AssetInfo.empty()

    def get_ohlc_data_for_asset(self, asset_pair: str, interval: int) -> Dict[int, OHLCData]:
        """Download OHLC data for given asset pair from kraken
        :param asset_pair: asset pair to get OHLC data for
        :param interval: time frame interval in minutes (optional): 1 (default), 5, 15, 30, 60, 240, 1440, 10080, 21600
        :param since: return committed OHLC data since given id (optional.  exclusive)
        """
        values = {'pair': asset_pair, 'interval': interval}  # , 'since': since}
        response = self.query_public('OHLC', values)
        data = response['result']
        if asset_pair in data:
            data_points = data[asset_pair]
            return {int(p[0]): OHLCData(open_price=float(p[1]),
                                        high_price=float(p[2]),
                                        low_price=float(p[3]),
                                        close_price=float(p[4]),
                                        volume_weighted_average_price=float(p[5]),
                                        volume=float(p[6]),
                                        count=float(p[7])) for p in data_points}
        return dict()
