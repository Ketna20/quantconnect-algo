# region imports
from AlgorithmImports import *
# endregion

class BuyAndHold(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2020, 1, 1)
        self.set_end_date(2021, 1, 1)
        self.set_cash(10000)
        self.add_equity("XOM", Resolution.Daily)
        

    def on_data(self, data: Slice):
        if not self.portfolio.invested:
            self.set_holdings("XOM", 1)
    
