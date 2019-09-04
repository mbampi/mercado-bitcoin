
from mbtc.Coin import Coin


class Account:

    def __init__(self, bch=None, brl=None, btc=None, eth=None, ltc=None, xrp=None):
        self.bch = bch
        self.brl = brl
        self.btc = btc
        self.eth = eth
        self.ltc = ltc
        self.xrp = xrp

    @staticmethod
    def from_json(json):
        bch = Coin.from_json('bch', json)
        brl = Coin.from_json('brl', json)
        btc = Coin.from_json('btc', json)
        eth = Coin.from_json('eth', json)
        ltc = Coin.from_json('ltc', json)
        xrp = Coin.from_json('xrp', json)

        return Account(bch, brl, btc, eth, ltc, xrp)

