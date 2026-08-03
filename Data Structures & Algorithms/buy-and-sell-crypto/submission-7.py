class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l, r = 0, 0

        while l < len(prices) - 1:
            prof = max(prof, prices[r] - prices[l])
            if(l == r):
                r += 1
                continue
            elif(r == len(prices) - 1):
                l += 1
                continue
            else:
                if(prices[r+1] > prices[r]):
                    r += 1
                    continue
                if(prices[l+1] < prices[l]):
                    l += 1
                    continue
                if(prices[r+1] < prices[l]):
                    l = r+1
                    r += 1
                    continue
                r += 1

        return prof
                
                


        