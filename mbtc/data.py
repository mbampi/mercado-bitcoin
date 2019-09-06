
import datetime as dt


class Last24:

    def __init__(self, json):
        json = json['ticker']
        date_json = json['date']
        date_json = dt.datetime.utcfromtimestamp(date_json)

        self.high = json['high']
        self.low = json['low']
        self.vol = json['vol']
        self.last = json['last']
        self.buy = json['buy']
        self.sell = json['sell']
        self.date = date_json.date()
        self.time = date_json.time()

    def __str__(self):
        s = "Last 24h from " + str(self.date) + " at " + str(self.time) + ":"
        s += "\n  last trade: " + self.last
        s += "\n  low: " + self.low + " | high: " + self.high
        s += "\n  buy: " + self.buy + " | sell: " + self.sell
        s += "\n  volume: " + self.vol
        return s


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

    def __str__(self):
        s = "Day Summary from " + str(self.date) + ":"
        s += "\n  opening: " + self.opening + " | closing: " + self.closing
        s += "\n  lowest: " + self.lowest + " | highest: " + self.highest
        s += "\n  volume: " + self.volume
        s += "\n  quantity: " + self.quantity
        s += "\n  amount: " + self.amount
        s += "\n  avg_price: " + self.avg_price
        return s
