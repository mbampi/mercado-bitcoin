

class Coin:

    def __init__(self, coin, response_data):
        balance = response_data['balance'][coin]
        withdrawal_limits = response_data['balance'][coin]

        self.available = balance['available']
        self.total = balance['total']
        self.amount_open_orders = balance['amount_open_orders']
        self.withdrawal_limit_available = withdrawal_limits['available']
        self.withdrawal_limit_total = withdrawal_limits['total']
