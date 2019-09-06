
import hashlib
import hmac
import http.client
import json
import urllib.parse
import time
from collections import OrderedDict


class TradeAPI:

    def __init__(self, tapi_id, tapi_secret):
        self.MB_TAPI_ID = tapi_id
        self.MB_TAPI_SECRET = tapi_secret
        self.REQUEST_HOST = 'www.mercadobitcoin.net'
        self.REQUEST_PATH = '/tapi/v3/'

    @staticmethod
    def __generate_nonce():
        tapi_nonce = str(int(time.time()))
        return tapi_nonce

    def __generate_mac(self, params):
        params_string = self.REQUEST_PATH + '?' + params
        h = hmac.new(self.MB_TAPI_SECRET, digestmod=hashlib.sha512)
        h.update(params_string)
        tapi_mac = h.hexdigest()
        return tapi_mac

    def __generate_headers(self, tapi_mac):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'TAPI-ID': self.MB_TAPI_ID,
            'TAPI-MAC': tapi_mac
        }
        return headers

    def __request(self, params, headers):
        try:
            conn = http.client.HTTPSConnection(self.REQUEST_HOST)
            conn.request("POST", self.REQUEST_PATH, params, headers)

            response = conn.getresponse()
            response = response.read()

            # É fundamental utilizar a classe OrderedDict para preservar a ordem dos elementos
            response_json = json.loads(response, object_pairs_hook=OrderedDict)
        finally:
            if conn:
                conn.close()
        return response_json

    # ------------ METHODS ------------

    def list_system_messages(self, level=None):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'list_system_messages',
            'tapi_nonce': tapi_nonce
        }
        if level is not None:
            method_params['level'] = level

        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def get_account_info(self):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'get_account_info',
            'tapi_nonce': tapi_nonce
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def get_order(self, coin_pair, order_id):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'get_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'order_id': order_id
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def list_orders(self, coin_pair, order_type=None, status_list=None, has_fills=None,
                    from_id=None, to_id=None, from_timestamp=None, to_timestamp=None):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'list_orders',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
        }
        if order_type is not None:
            method_params['order_type'] = order_type
        if status_list is not None:
            method_params['status_list'] = status_list
        if has_fills is not None:
            method_params['has_fills'] = has_fills
        if from_id is not None:
            method_params['from_id'] = from_id
        if to_id is not None:
            method_params['to_id'] = to_id
        if from_timestamp is not None:
            method_params['from_timestamp'] = from_timestamp
        if to_timestamp is not None:
            method_params['to_timestamp'] = to_timestamp

        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def list_orderbook(self, coin_pair, full=None):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'list_orderbook',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
        }
        if full is not None:
            method_params['full'] = full
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def place_buy_order(self, coin_pair, quantity, limit_price):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'place_buy_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'quantity': quantity,
            'limit_price': limit_price
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def place_sell_order(self, coin_pair, quantity, limit_price):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'place_sell_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'quantity': quantity,
            'limit_price': limit_price
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def place_market_buy_order(self, coin_pair, cost):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'place_market_buy_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'cost': cost,
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def place_market_sell_order(self, coin_pair, quantity):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'place_market_sell_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'quantity': quantity,
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def cancel_order(self, coin_pair, order_id):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'cancel_order',
            'tapi_nonce': tapi_nonce,
            'coin_pair': coin_pair,
            'order_id': order_id,
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def get_withdrawal(self, coin, withdrawal_id):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'get_withdrawal',
            'tapi_nonce': tapi_nonce,
            'coin': coin,
            'withdrawal_id': withdrawal_id,
        }
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response

    def withdraw_coin(self, coin, description=None):
        tapi_nonce = self.__generate_nonce()
        method_params = {
            'tapi_method': 'withdraw_coin',
            'tapi_nonce': tapi_nonce,
            'coin': coin,
        }
        if description is not None:
            method_params['description'] = description
        method_params = urllib.parse.urlencode(method_params)
        tapi_mac = self.__generate_mac(method_params)
        headers = self.__generate_headers(tapi_mac)

        response = self.__request(method_params, headers)
        return response
