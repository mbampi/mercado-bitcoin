
from mbtc import config


class TradeAPI:

    # Constants
    REQUEST_PATH = '/tapi/v3/'
    MB_TAPI_SECRET = config.MB_TAPI_SECRET

    def place_buy_order(self, coin, quantity, limit_price):
        method_params = {
            'tapi_method': 'place_buy_order',
            'tapi_nonce': '1',
            'coin_pair': 'BRL' + coin,
            'quantity': quantity,
            'limit_price': limit_price
        }
        return method_params

    def place_sell_order(self, coin, quantity, limit_price):
        method_params = {
            'tapi_method': 'place_sell_order',
            'tapi_nonce': '1',
            'coin_pair': 'BRL' + coin,
            'quantity': quantity,
            'limit_price': limit_price
        }
        return method_params

    def list_orders(self, coin_pair, order_type=None, status_list=None):
        method_params = {
            'tapi_method': 'place_sell_order',
            'tapi_nonce': '1',
            'coin_pair': 'BRL' + coin,
            'quantity': quantity,
            'limit_price': limit_price
        }
        return method_params

    def get_account_info(self):
        method_params = {
            'tapi_method': 'get_account_info',
            'tapi_nonce': '1'
        }
        return method_params

    def generate_mac(self, params):
        params = urlencode(params)
        params_string = REQUEST_PATH + '?' + params
        H = hmac.new(MB_TAPI_SECRET.encode(), digestmod=hashlib.sha512)
        H.update(params_string.encode())
        tapi_mac = H.hexdigest()
        return tapi_mac
