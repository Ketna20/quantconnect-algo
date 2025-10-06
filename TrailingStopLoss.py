class TrailingStopLoss(QCAlgorithm):
    
    
    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetEndDate(2019, 1, 1)
        self.SetCash(100000)
        spy = self.AddEquity("SPY", Resolution.Daily)
        self.highest_price_seen = None
        self.sell_ticket = None
        self.invest = True
        
    def OnData(self, data):

        # CREATE INITIAL ORDER FOR 1 SHARE
        if not self.Portfolio.Invested and self.invest:
            # Note this is just buying a single share, not 100% portfolio
            self.MarketOrder("SPY", 1)
            self.invest = False
           
        # ONCE WE"VE INVESTED, CREATE STOPMARKETORDER FOR STOP LOSS 
        if self.Portfolio.Invested and self.sell_ticket == None:
            self.sell_ticket = self.StopMarketOrder("SPY", -1, 0.9 * self.Securities["SPY"].Close)
            self.highest_price_seen = self.Securities["SPY"].Close
        
        # IF STOPMARKETORDER EXISTS, CHECK FOR NEED TO UPDATE
        if self.sell_ticket != None:
            
            #1. Compare today's closing price to historical highest price
            if self.Securities["SPY"].Close > self.highest_price_seen:
                
                #2. Update highest price seen 
                self.highest_price_seen = self.Securities["SPY"].Close
                
                #3. Update Limit for StopMarketTicket
                updateFields = UpdateOrderFields()
                updateFields.StopPrice = self.highest_price_seen * 0.9
                response = self.sell_ticket.Update(updateFields)
                
                if response.IsSuccess:
                    self.Debug(f"Stop Price was updated to {self.highest_price_seen * 0.9} ")
                
    def OnOrderEvent(self, orderEvent):
        if orderEvent.Status != OrderStatus.Filled:
            return
        if self.sell_ticket is not None and self.sell_ticket.OrderId == orderEvent.OrderId: 
            self.Log("SELL TICKET ORDER EXECUTED")
