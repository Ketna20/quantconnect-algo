class SharesAndPriceInfo(QCAlgorithm):

    def Initialize(self):
        
        self.SetCash(100000)
        self.SetStartDate(2015,1,1) 
        self.SetEndDate(2020,1,1) 
        self.apple = self.AddEquity("AAPL", Resolution.Daily)
        self.invest_toggle = True
        self.sell_toggle = True
        
        
    def OnData(self, data):
        if not data[self.apple.Symbol]:
          return

        if not self.Portfolio.Invested and self.invest_toggle:
          
          # data[self.apple.Symbol].Open -> get the opening price for AAPL
          shares_to_buy = int(self.Portfolio.Cash/data[self.apple.Symbol].Open)
          self.MarketOrder(self.apple.Symbol, shares_to_buy)
          
          self.invest_toggle = False
          return

        profit = self.Portfolio[self.apple.Symbol].UnrealizedPercent

        if profit >= 0.1 and self.sell_toggle
          # 10% profit is reached, sell half our shares
          held_shares = self.Portfolio[self.apple.Symbol].Quantity

          self.MarketOrder(self.apple.Symbol, -(held_shares//2))
          self.sell_toggle = False


  def OnOrderEvent(self, orderEvent):

    if(orderEvent.FillQuantity == 0:
      return

    fetched = self.Transactions.GetOrderById(orderEvent.OrderId)

    self.Log(f"{str(fetched.Type)} was filled")
    self.Log(f"Symbol was : {str(orderEvent.Symbol)} was filled")
    self.Log(f"Quantity was : {str(orderEvent.FillQuantity)} was filled")








  
      
