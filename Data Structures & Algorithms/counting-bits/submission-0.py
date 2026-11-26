class Solution:
    def countBits(self, n: int) -> List[int]:
        

        def bit_counter(n):
            counter = 0
            while n > 0:
                if n % 2 == 1:
                    counter += 1
                    n -= 1
                    n /= 2
                else:
                    n/= 2
            
            return counter
        sol = []
        for n in range(n + 1):
            sol.append(bit_counter(n))

        return sol