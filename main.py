from data_import import Data
from data_wrangle import Wrangle
from visualize import Visualize
from reinforce import Reinforce

if __name__ == '__main__' :
    """
    customize the data_dir if you intend to utilize the dataset you've downloaded previously.
    You should at least enter in 'C:/' or an existing directory to keep the code running.
    
    TICKER's should be in uppercase
    
    API_KEY refers to the Quandl API token. Create an account if you do not have access to tokens
    Quandl signin URL : https://www.quandl.com/sign-up-modal?defaultModal=showSignUp
    If you plan to use data stored locally, you may leave the API_KEY as it is.
    """
    data_dir = 'D:/rawDataFiles/stock_data'
    TICKER = 'AAPL'
    API_KEY = ''

    data = Data(TICKER, API_KEY, data_dir)
    print(str(data.ticker)+"'s raw data shape is "+str(data.data.shape))

    wrangled = Wrangle(data.data)
    print(str(data.ticker)+"'s wrangled data head(5) is as follows")
    print(wrangled.data.head(5))

    #visualize = Visualize(wrangled.data)

    #reinforce = Reinforce(wrangled.data)