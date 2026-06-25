class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while(n != 0):
            if(n % 2 == 1):
                n -= 1
                total += 1
            else:
                n /= 2
                total += 1

        return int(total / 2)