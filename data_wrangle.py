import numpy as np

"""
I mainly referenced a published book, '파이썬과 케라스를 이용한 딥러닝/강화학습 주식투자'

book URL : http://wikibook.co.kr/deep-learning-trading/'
"""

class Wrangle :
    def __init__(self, data):
        """
        This class adds preprocessed data into the dataset
        The added data includes
        close_ma : close price moving average of [5, 10, 20, 60, 120]
        volume_ma : volume moving average of [5, 10, 20, 60, 120]
        open_lastclose_ratio : ratio between open price and last period's close price
        high_close_ratio : ratio between high price and close price
        low_close_ratio : ratio between low price and close price
        close_lastclose_ratio : ratio between close price and last period's close price
        vol_lastvol_ratio : ratio between volume and last period's volume
        bollinger_band : the upper and lower boundaries of the bollinger band. I used a standard 20-day bollinger band
        """
        self.data = data
        self.moving_average()
        self.ratio()
        self.bollinger_band()

    def moving_average(self):
        windows = [5, 10, 20, 60, 120]
        self.close_ma(windows)
        self.volume_ma(windows)

    def close_ma(self, windows):
        close = self.data['Adj. Close']
        pads = list()

        for i in range(120):
            pads.append(np.mean(list(close)[:i+1]))

        for window in windows :
            ma = list(close.rolling(window).mean())
            for i in range(window):
                ma[i] = pads[i]
            self.data['Close_MA{}'.format(window)] = ma

    def volume_ma(self, windows):
        volume = self.data['Adj. Volume']
        pads = list()

        for i in range(120):
            pads.append(np.mean(list(volume)[:i+1]))

        for window in windows :
            ma = list(volume.rolling(window).mean())
            for i in range(window):
                ma[i] = pads[i]
            self.data['Volume_MA{}'.format(window)] = ma

    def ratio(self):
        self.open_lastclose_ratio()
        self.high_close_ratio()
        self.low_close_ratio()
        self.close_lastclose_ratio()
        self.vol_lastvol_ratio()

    def open_lastclose_ratio(self):
        self.data['open_lastclose_ratio'] = np.zeros(len(self.data))
        self.data['open_lastclose_ratio'].iloc[1:] = \
            (self.data['Adj. Open'][1:].values  - self.data['Adj. Close'][:-1].values)/self.data['Adj. Close'][:-1].values

    def high_close_ratio(self):
        self.data['high_close_ratio'] = \
            (self.data['Adj. High'].values - self.data['Adj. Close'].values)/self.data['Adj. Close'].values

    def low_close_ratio(self):
        self.data['low_close_ratio'] = \
            (self.data['Adj. Low'].values - self.data['Adj. Close'].values)/self.data['Adj. Close'].values

    def close_lastclose_ratio(self):
        self.data['close_lastclose_ratio'] = np.zeros(len(self.data))
        self.data['close_lastclose_ratio'].iloc[1:] = \
            (self.data['Adj. Close'][1:].values  - self.data['Adj. Close'][:-1].values)/self.data['Adj. Close'][:-1].values

    def vol_lastvol_ratio(self):
        self.data['vol_lastvol_ratio'] = np.zeros(len(self.data))
        self.data['vol_lastvol_ratio'].iloc[1:] = \
            (self.data['Adj. Volume'][1:].values  - self.data['Adj. Volume'][:-1].values)/self.data['Adj. Volume'][:-1].values

    def bollinger_band(self):
        close = self.data['Adj. Close']
        pads = list()

        for i in range(20):
            pads.append(np.std(list(close)[:i+1]))

        std = self.data['Adj. Close'].rolling(window=20).std()
        std[:20] = pads

        self.data['bollinger_upper'] = self.data['Close_MA20'] + 2 * std
        self.data['bollinger_lower'] = self.data['Close_MA20'] - 2 * std