class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0  
        
        profit = 0

        current_stock = prices[0]

        for n in prices:
            if n > current_stock:
                profit += n - current_stock
            
            current_stock = n
        
        return profit
                

