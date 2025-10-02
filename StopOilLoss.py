class StopOilLOss(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Start on 1.1.2015
        self.SetEndDate(2021, 1, 1)  # Start on 1.1.2015
        self.SetCash(100000)  #  10,000$ are available
        
        self.xom = self.AddEquity("XOM", Resolution.Daily)
        self.bp = self.AddEquity("BP",Resolution.Daily)
        self.invest_toggle = True
        self.order_toggle = True

    def OnData(self, data):
 

        if not self.Portfolio.Invested and self.invest_toggle:
            
            self.SetHoldings(self.xom.Symbol,0.5)
            self.SetHoldings(self.bp.Symbol,0.5)
            self.invest_toggle = False
            
        if self.Portfolio.Invested and self.order_toggle:
            xom_shares = self.Portfolio[self.xom.Symbol].Quantity
            xom_buy_price = self.Portfolio[self.xom.Symbol].Price
            bp_shares = self.Portfolio[self.bp.Symbol].Quantity
            bp_buy_price = self.Portfolio[self.bp.Symbol].Price
            self.StopMarketOrder(self.xom.Symbol,-xom_shares,xom_buy_price*0.8)
            self.StopMarketOrder(self.bp.Symbol,-bp_shares,bp_buy_price*0.8)
            self.order_toggle = False
