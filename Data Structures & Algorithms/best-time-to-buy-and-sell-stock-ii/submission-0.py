class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        current_stock = prices[0]

        for n in prices:
            if n > current_stock:
                profit += n - current_stock
                current_stock = n
            else:
                current_stock = n
        
        return profit
                

