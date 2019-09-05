
import requests


class DataAPI:

    @staticmethod
    def __request(coin, method, params=None):
        url = 'https://www.mercadobitcoin.net/api'
        url += '/' + coin + '/' + method
        if params is not None:
            url += '/' + params

        response = requests.get(url)
        return response.json()

    @staticmethod
    def ticker(coin):
        method = 'ticker'
        resp = DataAPI.__request(coin, method)
        return resp

    @staticmethod
    def orderbook(coin):
        method = 'orderbook'
        resp = DataAPI.__request(coin, method)
        return resp

    @staticmethod
    def trades(coin, since_id=None, from_timestamp=None, to_timestamp=None):
        method = 'orderbook'
        params = None

        # Check parameters
        if since_id is not None:
            params = "?since=" + since_id
        elif from_timestamp is not None:
            params = from_timestamp
            if to_timestamp is not None:
                params += '/' + to_timestamp

        resp = DataAPI.__request(coin, method, params)
        return resp

    @staticmethod
    def day_summary(coin, day=None, month=None, year=None):
        method = "day-summary"

        # Check parameters
        if None not in [day, month, year]:
            params = year + "/" + month + "/" + day
        else:
            params = None

        resp = DataAPI.__request(coin, method, params)
        return resp
