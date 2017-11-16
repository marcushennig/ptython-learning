class OHLCData:

    def __init__(self, time: int, open: float, high: float, low: float, close: float, vwap: float, volume: int, count: int):
        """ Define data point in open-high-low-close chart"""
        self.time = time        # Time
        self.open = open        # Start result of the time unit's price action
        self.high = high        # Highest price over unit of time
        self.low = low          # Lowest price over unit of time
        self.close = close      # End result of the time unit's price action
        self.vwap = vwap        #
        self.volume = volume    # Traded volume over the time unit
        self.count = count      #

    def __str__(self):
        return f'(time: {self.time}, ' \
               f'open: {self.open}, ' \
               f'high: {self.high}, ' \
               f'low: {self.low}, '\
               f'vwap: {self.vwap}, '\
               f'volume: {self.volume}, '\
               f'count: {self.count})'

    @staticmethod
    def empty():
        return OHLCData(time=0, open=0, high=0, low=0, close=0, vwap=0, volume=0, count=0)
