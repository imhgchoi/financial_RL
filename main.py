from data_import import Data
from data_wrangle import Wrangle
from visualize import Visualize
from environment import Environment
from agent import Agent
from reinforce import Reinforce



if __name__ == '__main__' :
    """
    customize the data_dir if you intend to utilize the dataset you've downloaded previously.
    You should at least enter in 'C:/' or an existing directory to keep the code running.
    
    TICKER's should be in uppercase
    
    API_KEY refers to the Quandl API token. Create an account if you do not have access to tokens
    Quandl signin URL : https://www.quandl.com/sign-up-modal?defaultModal=showSignUp
    If you plan to use data stored locally, you may leave the API_KEY as it is.
    
    The INITIAL_BALANCE refers to the amount of money in dollars you want to start in trading in an episode.
    """
    data_dir = 'D:/rawDataFiles/stock_data'
    TICKER = 'AAPL'
    API_KEY = ''

    INITIAL_BALANCE = 0

    data = Data(TICKER, API_KEY, data_dir)
    print(str(data.ticker)+"'s raw data shape is "+str(data.data.shape))

    wrangled = Wrangle(data.data)
    print(str(data.ticker)+"'s wrangled data head(5) is as follows")
    print(wrangled.data.head(5))

    visualize = Visualize(wrangled.data)


    environment = Environment(wrangled.data)
    agent = Agent(environment, INITIAL_BALANCE, min_trade=1, max_trade=5, delayed_reward_threshold=.05)
    #reinforce = Reinforce(wrangled.data)