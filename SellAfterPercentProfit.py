class SellAfterPercent(QCAlgorithm):

    def Initialize(self):
        
        self.SetCash(10000)
        self.SetStartDate(2015,1,1) 
        self.SetEndDate(2020,1,1) 
        self.brkb = self.AddEquity("BRK.B", Resolution.Daily)
        self.invest = True
        
        
    def OnData(self, data):
        
        if not self.Portfolio.Invested and self.invest:  # If not invested, invest everything in Apple
            self.SetHoldings("BRK.B", 1) 
            self.invest = False
        
        # Grab Portfolio Attributes
        
        profit  = self.Portfolio['BRK.B'].UnrealizedProfitPercent 
        self.Log(profit)
         
        if profit >= 0.2:
            self.Liquidate("BRK.B") 
