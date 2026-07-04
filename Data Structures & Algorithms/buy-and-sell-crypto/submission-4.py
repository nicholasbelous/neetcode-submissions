class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        buy , sell = 0 , 1

        while(sell < len(prices)):
            prof = max(prices[sell] - prices[buy], prof)

            if(sell == (len(prices) - 1)):
                while(buy < sell):
                    buy += 1
                    prof = max(prices[sell] - prices[buy], prof)

                break

            if((sell - buy) == 1):
                sell += 1
                continue
            
            if((prices[sell + 1] - prices[buy]) > (prices[sell] - prices[buy + 1])):
                sell += 1
            elif((prices[sell + 1] - prices[buy]) < (prices[sell] - prices[buy + 1])):
                buy += 1
            else:
                sell += 1

        prof = max(prices[sell] - prices[buy], prof)

        return prof