import logging
from Kraken.kraken_api import KrakenAPI

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)

kraken = KrakenAPI()
info = kraken.get_ohlc_data_for_asset('XETHZEUR', 1)

print(info)