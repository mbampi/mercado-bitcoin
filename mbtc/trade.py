"""
Mercado Bitcoin  -  API de Negociações v3

https://www.mercadobitcoin.com.br/trade-api/

O acesso à API é limitado por padrão ao máximo de 60 requisições a cada 60 segundos, por usuário.
"""


from urllib.parse import urlencode
import hashlib
import hmac
import datetime
from mbtc import config








