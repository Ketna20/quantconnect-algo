# region imports
from AlgorithmImports import *
# endregion

class BuyAndSellEquities(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2021, 1, 1)
        self.set_cash(10000)
        self.add_equity("KO", Resolution.Daily)
        self.invest = True
        

    def on_data(self, data: Slice):
        if not self.portfolio.invested and self.invest: # If not invested, invest everything in KO
            self.set_holdings("KO", 0.5)
            self.invested_time = self.Time
        
        # as the self.Time object in quantconnect is a python datetime object, we can simply substract
      # the current time from the invest time and sell if e.g 100 days have passed
        time_diff = (self.Time - self.invested_time).days
        self.Log(time_diff)

        if time_diff > 100:
            self.Liquidate("KO")
            self.invest = False
