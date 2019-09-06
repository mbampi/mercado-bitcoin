
from mbtc import DataAPI
from mbtc.Coin import Coin

import json
import pandas as pd
import time
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def day_to_dataframe():
    df = pd.DataFrame(columns=['date', 'opening', 'closing', 'lowest', 'highest',
                               'volume', 'quantity', 'amount', 'avg_price'])
    start_date = date(2019, 1, 1)
    end_date = date(2019, 9, 5)
    for d in daterange(start_date, end_date):
        btc_day = DataAPI.day_summary(Coin.Bitcoin, d.year, d.month, d.day).json().values()
        df.loc[len(df)] = list(btc_day)
        time.sleep(2)

    print(df.to_string)
    df.to_csv("bitcoin_daily" + ".csv")


print("Bitcoin DataAPI")
day_to_dataframe()


