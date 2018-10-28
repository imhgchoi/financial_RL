import tensorflow as tf

"""
I mainly referenced a published book, '파이썬과 케라스를 이용한 딥러닝/강화학습 주식투자'

book URL : http://wikibook.co.kr/deep-learning-trading/'
"""

class Reinforce :
    def __init__(self, wrangled):
        self.train = wrangled[:1]
        self.val = wrangled[1:2]
        self.test = wrangled[2:]

        while True :
            model = self.train()
            metric = self.evaluate(model)
            if metric > 2 :
                self.save_model(model)
                break
            else :
                continue

    def train(self):
        model = 1
        return model

    def evaluate(self, model):
        self.validate(model)
        self.test(model)
        metric = 1

        return metric

    def validate(self, model):
        pass

    def test(self, model):
        pass

    def save_model(self, model):
        pass