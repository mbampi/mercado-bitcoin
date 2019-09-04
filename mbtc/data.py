import requests
import datetime as dt
from mbtc.DataAPI import DataAPI


class Last24:
    def __init__(self):
        last24_json = request_last_24h()
        last24_json = last24_json['ticker']
        date_json = last24_json['date']
        date_json = dt.datetime.utcfromtimestamp(date_json)

        self.high = last24_json['high']
        self.low = last24_json['low']
        self.vol = last24_json['vol']
        self.last = last24_json['last']
        self.buy = last24_json['buy']
        self.sell = last24_json['sell']
        self.date = date_json.date()
        self.time = date_json.time()

    def __str__(self):
        saida = "Last 24h from " + str(self.date) + " at " + str(self.time) + ":"
        saida += "\n  last trade: " + self.last
        saida += "\n  low: " + self.low + " | high: " + self.high
        saida += "\n  buy: " + self.buy + " | sell: " + self.sell
        saida += "\n  volume: " + self.vol
        return saida


class DaySummary:

    def __init__(self, date, opening, closing, lowest, highest, volume, quantity, amount, avg_price):
        self.date = date
        self.opening = opening
        self.closing = closing
        self.lowest = lowest
        self.highest = highest
        self.volume = volume
        self.quantity = quantity
        self.amount = amount
        self.avg_price = avg_price

    @staticmethod
    def from_json(json):
        date = json['date']
        opening = json['opening']
        closing = json['closing']
        lowest = json['lowest']
        highest = json['highest']
        volume = json['volume']
        quantity = json['quantity']
        amount = json['amount']
        avg_price = json['avg_price']

        return DaySummary(date, opening, closing, lowest, highest, volume, quantity, amount, avg_price)

    @staticmethod
    def request(coin, day=None, month=None, year=None):

        if all(v is not None for v in [day, month, year]):
            params = "/" + year + "/" + month + "/" + day
        else:
            params = None

        resp = DataAPI.request_data(coin, "day-summary", params)
        return resp

    def __str__(self):
        saida = "Day Summary from " + str(self.date) + ":"
        saida += "\n  opening: " + self.opening + " | closing: " + self.closing
        saida += "\n  lowest: " + self.lowest + " | highest: " + self.highest
        saida += "\n  volume: " + self.volume
        saida += "\n  quantity: " + self.quantity
        saida += "\n  amount: " + self.amount
        saida += "\n  avg_price: " + self.avg_price
        return saida


def request_last_24h(coin):
    COIN = coin
    METHOD = 'ticker'
    url = 'https://www.mercadobitcoin.net/api/' + COIN + '/' + METHOD + '/'
    req = requests.get(url)
    return req.json()
