class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = testBuy = testSell = prices[0] 


        for num in prices:
            prof = sell - buy
            
            if(num > sell):
                sell = num
                
            if(num < testBuy):
                testBuy = num
                testSell = num
            
            testSell = num

            testProf = testSell - testBuy
            if(testProf > prof):
                buy = testBuy
                sell = testSell

        return sell - buy