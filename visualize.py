import matplotlib.pyplot as plt
import mpl_finance as mplfin
import os

class Visualize :
    def __init__(self, wrangled):
        self.candle_stick(wrangled)
        self.moving_average(wrangled)
        self.bollinger_bands(wrangled)
        self.ratios(wrangled)

    def candle_stick(self, wrangled):
        fig = plt.figure(figsize = (17,3))
        ax = fig.add_subplot(1,1,1)
        mplfin.candlestick2_ohlc(ax, width=1, colorup='r', colordown='b',
                                 opens = wrangled['Adj. Open'], highs = wrangled['Adj. High'],
                                 lows = wrangled['Adj. Low'], closes = wrangled['Adj. Close'])
        plt.savefig(str(os.getcwd()).replace('\\','/')+'/images/candlestick.png')
        plt.close()

    def moving_average(self, wrangled):
        fig = plt.figure(figsize = (17,3))
        ax = fig.add_subplot(1,1,1)
        ax.plot(wrangled['Adj. Close'], color='black', linewidth=0.8)
        ax.plot(wrangled['Close_MA5'], label='ma5', color='yellow', linewidth=0.5)
        ax.plot(wrangled['Close_MA10'], label='ma10', color='orange', linewidth=0.5)
        ax.plot(wrangled['Close_MA20'], label='ma20', color='red', linewidth=0.5)
        ax.plot(wrangled['Close_MA60'], label='ma60', color='blue', linewidth=0.5)
        ax.plot(wrangled['Close_MA120'], label='ma120', color='green', linewidth=0.5)
        plt.legend()
        plt.savefig(str(os.getcwd()).replace('\\','/')+'/images/moving_average.png')
        plt.close()

    def bollinger_bands(self, wrangled):
        fig = plt.figure(figsize = (17,3))
        ax = fig.add_subplot(1,1,1)
        ax.plot(wrangled['Adj. Close'], color='black', linewidth=0.8)
        ax.plot(wrangled['bollinger_upper'], label='upper', color='red', linewidth=0.5)
        ax.plot(wrangled['bollinger_lower'], label='lower', color='blue', linewidth=0.5)
        plt.legend()
        plt.savefig(str(os.getcwd()).replace('\\','/')+'/images/bollinger_band.png')
        plt.close()

    def ratios(self, wrangled):
        fig = plt.figure(figsize = (17,3))
        ax = fig.add_subplot(1,1,1)
        ax.plot(wrangled['close_lastclose_ratio'], color='black', linewidth=0.8)
        plt.savefig(str(os.getcwd()).replace('\\','/')+'/images/close_lastclose_ratio.png')
        plt.close()

        fig = plt.figure(figsize = (17,3))
        ax = fig.add_subplot(1,1,1)
        ax.plot(wrangled['vol_lastvol_ratio'], color='black', linewidth=0.8)
        plt.savefig(str(os.getcwd()).replace('\\','/')+'/images/vol_lastvol_ratio.png')
        plt.close()