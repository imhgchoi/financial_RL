
"""
I mainly referenced a published book, '파이썬과 케라스를 이용한 딥러닝/강화학습 주식투자'

book URL : http://wikibook.co.kr/deep-learning-trading/'
"""

class Environment:
    def __init__(self, dataset=None):
        self.dataset = dataset
        self.timestamp = 0
        self.observation = self.observe()

    def reset(self):
        self.observation = None
        self.timestamp = 0

    def observe(self):
        if self.timestamp < self.dataset.shape[0] :
            self.observation = self.dataset.iloc[self.timestamp]
            self.timestamp += 1
            return self.observation
        else :
            print('Episode Finished')
            return None

    def current_price(self):
        if self.observation is not None :
            return self.observation['Adj. Close']
        else:
            print('No observation found')
            return None
