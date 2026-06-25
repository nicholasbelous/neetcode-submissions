class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1

        total = 0
        while(n > 1):
            if(n % 2 == 0):
                total += 2
                n -= 1
            else:
                total += 1
                n -= 1

        
        return total

        
        