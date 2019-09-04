
import requests


class DataAPI:

    METHODS = ["ticker",
               "orderbook",
               "trades",       # /?since=<since> OR /<from> OR /<from>/<to>
               "day-summary"]  # /<year>/<month>/<day>

    URL = 'https://www.mercadobitcoin.net/api/'

    @staticmethod
    def request_data(coin, method, params=None):

        if params is None:
            url = DataAPI.URL + coin + method
        else:
            url = DataAPI.URL + coin + method + params

        response = requests.get(url)
        return response.json()
