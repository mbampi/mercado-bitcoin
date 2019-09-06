
from mbtc import DataAPI
from mbtc.Coin import Coin
import json


print("Bitcoin DataAPI")
r = DataAPI.day_summary(Coin.Bitcoin, 2019, 6, 8)
print(json.dumps(r.json(), indent=4))
