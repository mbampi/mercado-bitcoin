
from mbtc import DataAPI
from mbtc.Constants import Coin

import time
from datetime import timedelta, date
import datetime as dt

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def bitcoin_history(start_date, end_date):
    df = pd.DataFrame(columns=['date', 'opening', 'closing', 'lowest', 'highest',
                               'volume', 'quantity', 'amount', 'avg_price'])
    for d in date_range(start_date, end_date):
        btc_day = DataAPI.day_summary(Coin.Bitcoin, d.year, d.month, d.day).json().values()
        df.loc[len(df)] = list(btc_day)
        time.sleep(1)
    return df


def plot_candlestick(dataframe):
    dataframe['date'] = [mdates.date2num(dt.datetime.strptime(d, '%Y-%m-%d').date()) for d in dataframe['date']]
    quotes = [tuple(x) for x in dataframe[['date', 'opening', 'highest', 'lowest', 'closing']].values]

    fig, ax = plt.subplots()
    candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Bitcoin')

    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gcf().autofmt_xdate()
    plt.autoscale(tight=True)
    plt.show()


if __name__ == "__main__":
    print("Bitcoin DataAPI")

    # start = date(2017, 1, 1)
    # end = date.today()
    # df = bitcoin_history(start, end)
    # df.to_csv("bitcoin_daily" + ".csv")

    # df = pd.read_csv("bitcoin_daily" + ".csv", index_col=0)
    # plot_candlestick(df)




