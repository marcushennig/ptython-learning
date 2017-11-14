from Kraken.KrakenAPI import KrakenAPI

kraken = KrakenAPI()

result = kraken.get_asset_info('XETH')
print(result)
