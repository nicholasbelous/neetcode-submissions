class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        buy , sell = 0 , 1

        while(sell != (len(prices) -1 ) and buy != (len(prices) - 2)):
            prof = max(prices[sell] - prices[buy], prof)

            if(sell == (len(prices) -1 )):
                buy += 1
                continue
            
            if((sell - buy) == 1):
                sell += 1
                continue
            
            if((prices[sell + 1] - prices[buy]) > (prices[sell] - prices[buy + 1])):
                sell += 1
                continue
            elif((prices[sell + 1] - prices[buy]) < (prices[sell] - prices[buy + 1])):
                buy += 1
            else:
                sell += 1

        prof = max(prices[sell] - prices[buy], prof)

        return prof