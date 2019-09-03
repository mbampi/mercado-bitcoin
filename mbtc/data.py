import requests
import datetime as dt


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

    def __init__(self, day, month, year):
        day_sum = request_day_summary(day, month, year)
        self.date = day_sum['date']
        self.opening = day_sum['opening']
        self.closing = day_sum['closing']
        self.lowest = day_sum['lowest']
        self.highest = day_sum['highest']
        self.volume = day_sum['volume']
        self.quantity = day_sum['quantity']
        self.amount = day_sum['amount']
        self.avg_price = day_sum['avg_price']

    def __str__(self):
        saida = "Day Summary from " + str(self.date) + ":"
        saida += "\n  opening: " + self.opening + " | closing: " + self.closing
        saida += "\n  lowest: " + self.lowest + " | highest: " + self.highest
        saida += "\n  volume: " + self.volume
        saida += "\n  quantity: " + self.quantity
        saida += "\n  amount: " + self.amount
        saida += "\n  avg_price: " + self.avg_price
        return saida


def request_day_summary(day, month, year):
    """
    Given dat, month and year, returns json with full-day data
    :param day: int
    :param month: int
    :param year: int
    :return: json data as example
    {
    'date': '2013-06-20',
    'opening': 262.99999,
    'closing': 269.0,
    'lowest': 260.00002,
    'highest': 269.0,
    'volume': 7253.1336356785,
    'quantity': 27.11390588,
    'amount': 28,
    'avg_price': 267.5060416518087
    }
    """
    url = 'https://www.mercadobitcoin.net/api/coin/day-summary/' + year + '/' + month + '/' + day + '/'
    req = requests.get(url)
    return req.json()


def request_last_24h():
    """
    :return: json data as example from the last 24h
    {
    'ticker': {
        'high': 14481.47000000,
        'low': 13706.00002000,
        'vol': 443.73564488,
        'last': 14447.01000000,
        'buy': 14447.00100000,
        'sell': 14447.01000000,
        'date': 1502977646
    }
    }
    """
    COIN = 'BTC'
    METHOD = 'ticker'
    url = 'https://www.mercadobitcoin.net/api/' + COIN + '/' + METHOD + '/'
    req = requests.get(url)
    return req.json()
