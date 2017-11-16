from Kraken.kraken_api import KrakenAPI

kraken = KrakenAPI()

data = kraken.get_ohlc_data_for_asset('XETHZEUR', 1)
print(data)