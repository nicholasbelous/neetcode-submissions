class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1

        total = 0
        while(n > 1):
            total += (n - 2)
            n -= 1

        total += 2

        return total

        
        