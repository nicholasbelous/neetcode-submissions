from collections import deque

class StockSpanner:

    def __init__(self):
        self.prev_stock_prices = []

    def next(self, price: int) -> int:
        counter = 1

        #pointer to the stock price stack
        prev_stocks = list(self.prev_stock_prices)

        #added to the prev stock stack
        self.prev_stock_prices.append(price)

        while(prev_stocks):
            if(prev_stocks.pop() <= price):
                counter += 1
            else:
                break
            
        return counter
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)