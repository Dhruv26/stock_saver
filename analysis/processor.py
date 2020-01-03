import os
import pandas as pd
from datetime import date, timedelta
import quandl
from nsepy import get_quote, get_history
from talib import RSI, SMA, EMA, BBANDS


class TechAnalysis:

    def __init__(self, symbol='OIL'):
        self._symbol = symbol
        self._hist_prices = self.get_hist_prices()
        self._live_price = self.get_live_price()

    def get_live_price(self):
        return get_quote(self._symbol)['lastPrice']

    def get_hist_prices(self):
        # return quandl.get("NSE/{}".format(self._symbol), api_key="JQKKNh-2yVgdMKMbhxHu")
        today = date.today()
        cache_file = os.path.join('cache_prices', self._symbol + '_{}'.format(str(today)))
        if os.path.exists(cache_file):
            hist_prices = pd.read_pickle(cache_file)
        else:
            hist_prices = get_history(
                symbol=self._symbol, end=today, start=today - timedelta(days=(2 * 365)))
            hist_prices.to_pickle(cache_file)
        return hist_prices

    def get_sma(self, period):
        return SMA(self._hist_prices['Close'], timeperiod=period)

    def get_ema(self, period):
        return EMA(self._hist_prices['Close'], timeperiod=period)

    def get_rsi(self, period):
        return RSI(self._hist_prices['Close'], timeperiod=period)
