class AssetInfo:

    def __init__(self,
                 alternate_name: str,
                 asset_class: str,
                 decimals: int,
                 display_decimals: int):
        """Constructor for asset info object from Kraken"""
        self.alternate_name = alternate_name        # alternate name
        self.asset_class = asset_class              # asset class
        self.decimals = decimals                    # scaling decimal places
        self.display_decimals = display_decimals    # scaling decimal places for output display

    def __repr__(self):
        return "Test()"

    def __str__(self):
        return f'(alternate_name: {self.alternate_name}, ' \
               f'asset_class: {self.decimals}, ' \
               f'decimals: {self.decimals}, ' \
               f'display_decimals: {self.display_decimals})'

    @staticmethod
    def empty():
        return AssetInfo('', '', 0, 0)
