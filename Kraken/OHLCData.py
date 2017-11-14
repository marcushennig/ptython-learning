class OHLCData:

    def __init__(self):
        """ Define data point in open-high-low-close chart"""
        self.time = 0    # Time
        self.open = 0    # Start result of the time unit's price action
        self.high = 0    # Highest price over unit of time
        self.low = 0     # Lowest price over unit of time
        self.close = 0   # End result of the time unit's price action
        self.vwap = 0    #
        self.volume = 0  # Traded volume over the time unit
        self.count = 0   #
