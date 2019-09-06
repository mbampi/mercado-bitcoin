import requests


class DataAPI:

    @staticmethod
    def __request(coin, method, params=None):
        url = 'https://www.mercadobitcoin.net/api'
        url += '/' + str(coin) + '/' + method
        if params is not None:
            url += '/' + params

        response = requests.get(url)
        return response

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
        method = 'trades'
        params = None

        if since_id is not None:
            params = "?since=" + str(since_id)
        elif from_timestamp is not None:
            params = str(from_timestamp)
            if to_timestamp is not None:
                params += '/' + str(to_timestamp)

        resp = DataAPI.__request(coin, method, params)
        return resp

    @staticmethod
    def day_summary(coin, year, month, day):
        method = "day-summary"
        params = str(year) + '/' + str(month) + '/' + str(day)
        resp = DataAPI.__request(coin, method, params)
        return resp
