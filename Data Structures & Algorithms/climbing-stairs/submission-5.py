class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        
        total = 0
        a, b = 0, 1

        for _ in range(n):
            total = a + b
            newB = a + b
            a = b
            b = newB



        return total

        
        