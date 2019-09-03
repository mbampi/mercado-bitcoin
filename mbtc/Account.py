
from mbtc.Coin import Coin


class Account:

    def __init__(self, response_data):
        self.bch = Coin('bch', response_data)
        self.brl = Coin('brl', response_data)
        self.btc = Coin('btc', response_data)
        self.eth = Coin('eth', response_data)
        self.ltc = Coin('ltc', response_data)
        self.xrp = Coin('xrp', response_data)
