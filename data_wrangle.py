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

        """
        self.data = data
        self.moving_average()
        self.ratio()

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
        pass

    def open_lastclose_ratio(self):
        pass

    def high_close_ratio(self):
        pass

    def low_close_ratio(self):
        pass

    def

