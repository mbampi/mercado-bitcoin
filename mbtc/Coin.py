

class Coin:

    def __init__(self, available, total, amount_open_orders, withdrawal_limit_available, withdrawal_limit_total):
        self.available = available
        self.total = total
        self.amount_open_orders = amount_open_orders
        self.withdrawal_limit_available = withdrawal_limit_available
        self.withdrawal_limit_total = withdrawal_limit_total

    @staticmethod
    def from_json(coin, json):
        balance = json['balance'][coin]
        withdrawal_limits = json['balance'][coin]

        available = balance['available']
        total = balance['total']
        amount_open_orders = balance['amount_open_orders']
        withdrawal_limit_available = withdrawal_limits['available']
        withdrawal_limit_total = withdrawal_limits['total']

        return Coin(available, total, amount_open_orders, withdrawal_limit_available, withdrawal_limit_total)
