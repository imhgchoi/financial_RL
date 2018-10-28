import numpy as np

"""
I mainly referenced a published book, '파이썬과 케라스를 이용한 딥러닝/강화학습 주식투자'

book URL : http://wikibook.co.kr/deep-learning-trading/'
"""

class Agent:
    # trading costs combined
    fee = 0.00015
    tax = 0.003

    # actions
    BUY = 0
    SELL = 1
    HOLD = 2
    ACTIONS = [BUY, SELL, HOLD]
    ACTION_PROB = [1/3] * 3

    def __init__(self, environment, balance, min_trade=1, max_trade=5, delayed_reward_threshold=.05):
        """
        ---------------------
        parameters
        ---------------------
        initial balance : the amount of money in dollars you want to start in trading in an episode.
        current_balance : the amount of money in dollars you have in a certain state while trading. This gets updated
        stock_num : number of stocks you are holding
        portfolio_value : Total asset value you have.  = balance + (number of stocks) * (current stock price)
        base_pv : the portfolio value of the last investment period
        buy/sell/hold_num : To track trading history
        reward : the reward the agent receives for trading. 1 for positive returns, -1 for negative returns
        delayed_reward_threshold : the future goal of returns. By achieving this, the agent receives a delayed reward
        min_trade/max_trade : the boundary of the number of stocks the agent may trade at one time
        hold_ratio : the ratio of the number of stocks held to total holdable stock numbers
        portfolio_value_ratio : total portfolio_value compared to initial balance
        """
        self.environment = environment

        # DASHBOARD
        self.initial_balance = balance
        self.current_balance = balance
        self.stock_num = 0
        self.portfolio_value = 0
        self.base_pv = 0
        self.buy_num = 0
        self.sell_num = 0
        self.hold_num = 0
        self.reward = 0

        self.min_trade = min_trade
        self.max_trade = max_trade
        self.delayed_reward_threshold = delayed_reward_threshold

        # STATE VARIABLES
        self.hold_ratio = 0
        self.portfolio_value_ratio = 0


    def reset(self):
        self.current_balance = self.initial_balance
        self.stock_num = 0
        self.portfolio_value = self.current_balance + self.stock_num * self.environment.current_price()
        self.base_pv = self.portfolio_value
        self.buy_num = 0
        self.sell_num = 0
        self.hold_num = 0
        self.reward = 0
        self.hold_ratio = 0
        self.portfolio_value_ratio = 0

    def get_states(self):
        self.hold_ratio = self.stock_num / int(self.portfolio_value / self.initial_balance)
        self.portfolio_value_ratio = self.portfolio_value / self.initial_balance

        return (self.hold_ratio, self.portfolio_value_ratio)

    def decide_action(self, policy_network, sample, epsilon=0.1):
        if np.random.rand() < epsilon :
            exploration = True
            action = np.random.randint(3)
            confidence = 1/3
        else :
            exploration = False
            probs = policy_network.predict(sample)
            self.ACTION_PROB = probs
            action = np.argmax(probs)
            confidence = probs[action]

        return (action, confidence, exploration)

    def validate_action(self, action):
        if action == self.BUY :
            if self.current_balance < self.environment.current_price() * (1+self.fee) * self.min_trade :
                return False
        if action == self.SELL :
            if self.stock_num <= 0 :
                return False

    def decide_trading_amount(self, action, confidence):
        if action == self.HOLD :
            return 0
        else :
            return int(self.min_trade + (self.max_trade - self.min_trade) * confidence)


    def act(self, action, confidence):
        if not self.validate_action(action) :
            action = self.HOLD

        # Initialize immediate reward
        self.reward = 0
        current_price = self.environment.current_price()

        if action == self.BUY :
            self.buy(action, confidence, current_price)

        elif action == self.SELL :
            self.sell(action, confidence, current_price)

        elif action == self.HOLD :
            self.hold()

        self.portfolio_value = self.current_balance + current_price * self.stock_num
        returns = (self.portfolio_value - self.base_pv) / self.base_pv

        if returns > 0 :
            self.reward = 2
        elif returns == 0 :
            self.reward = 1
        elif returns < 0 :
            self.reward = -1

        if returns >= self.delayed_reward_threshold :
            delayed_reward = 2
            self.base_pv = self.portfolio_value
        elif returns <= - self.delayed_reward_threshold :
            delayed_reward = -2
            self.base_pv = self.portfolio_value
        else :
            delayed_reward = 0

        return (self.reward, delayed_reward)

    def buy(self, action, confidence, current_price):
        amount = self.decide_trading_amount(action, confidence)
        total_cost = current_price * amount * (1 + self.fee)
        if total_cost < self.current_balance:
            amount = max(min(int(self.current_balance / (current_price * (1 + self.fee))), self.max_trade),
                         self.min_trade)

        final_investment = current_price * amount * (1 + self.fee)
        self.current_balance -= final_investment
        self.stock_num += amount
        self.buy_num += 1

    def sell(self, action, confidence, current_price):
        amount = self.decide_trading_amount(action, confidence)
        if amount > self.stock_num :
            amount = self.stock_num
        total_retrieval = current_price * amount * (1 - self.fee - self.tax)

        self.current_balance += total_retrieval
        self.stock_num -= amount
        self.sell_num += 1

    def hold(self):
        self.hold_num += 1



