class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        for num in range(int(n**.5), 0, -1):
            if(2**n > n):
                pass
            n -= 2**n
            total += 1

        if(n == 1):
            total += 1
        return total