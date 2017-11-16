class OHLCData:

    def __init__(self,
                 open_price: float,
                 high_price: float,
                 low_price: float,
                 close_price: float,
                 volume_weighted_average_price: float,
                 volume: float,
                 count: float):
        """ Define data point in open-high-low-close chart"""
        self.open = open_price        # Start result of the time unit's price action
        self.high = high_price        # Highest price over unit of time
        self.low = low_price          # Lowest price over unit of time
        self.close = close_price      # End result of the time unit's price action
        self.vwap = volume_weighted_average_price        # Volume Weighted Average Price
        self.volume = volume            # Traded volume over the time unit
        self.count = count               #

    def __str__(self):
        return f'(open: {self.open}, ' \
               f'high: {self.high}, ' \
               f'low: {self.low}, '\
               f'vwap: {self.vwap}, '\
               f'volume: {self.volume}, '\
               f'count: {self.count})'

    @staticmethod
    def empty():
        return OHLCData(open_price=0,
                        high_price=0,
                        low_price=0,
                        close_price=0,
                        volume_weighted_average_price=0,
                        volume=0,
                        count=0)
