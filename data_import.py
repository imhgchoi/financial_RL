import quandl
import pandas as pd
import os

class Data :
    """
    This part of the code queries data from local disk or from the Quandl API.
    It first checks if there is pre-downloaded data from 2000-01-01 to 2017-12-31.
    If no file with the specified ticker exists, the Quandl API is referenced to download
    the financial technical data from 2000-01-01 to 2017-12-31.

    Quandl URL : https://www.quandl.com/tools/api
    """
    def __init__(self, ticker, api_key, data_dir):
        self.data_dir = data_dir
        self.colnames = ['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume', 'Split Ratio']
        self.ticker = ticker.replace(".", "_")
        self.key = api_key

        flag = self.search_local()

        if flag :
            self.api_query()

    def search_local(self):
        """
        search directory - if not there, return true; else if there, return false
        """
        files = os.listdir(self.data_dir)

        if self.ticker+'.csv' in files :
            self.data = pd.read_csv(self.data_dir + '/' + self.ticker + '.csv')[self.colnames]
            flag = False
        else :
            flag = True
        return flag

    def api_query(self):
        start = "2000-01-01"
        end = "2017-12-31"

        data = pd.DataFrame(quandl.get("WIKI/{}".format(self.ticker), start_date=start, end_date=end, api_key=self.key))
        self.data = data[self.colnames]