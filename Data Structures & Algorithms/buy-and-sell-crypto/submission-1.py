class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(not prices):
            return 0

        curMax = 0

        curBuy = prices[0]

        for n in range (1, len(prices)):
            profit = prices[n] - curBuy

            if(profit > curMax):
                curMax = profit
                continue
            elif(prices[n] < curBuy):
                curBuy = prices[n]
        
        return curMax
                