import matplotlib.pyplot as plt

class Visualize :
    def __init__(self, wrangled):
        plot = self.close_price()
        self.candle_stick(wrangled)
        self.moving_average(plot)
        self.save_plot(plot)


    def candle_stick(self, wrangled):
        pass

    def close_price(self):
        print("plot close price")
        plt = 1
        return plt

    def moving_average(self, plot):
        pass

    def save_plot(self, plot):
        pass