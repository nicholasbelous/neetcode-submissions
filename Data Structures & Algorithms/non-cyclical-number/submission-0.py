class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        total = 0
        seen = set()

        while total not in seen:
            for n in n_str:
                total += int(n) * int(n)
            if(total == 1):
                return True
            elif(total in seen):
                return False
            else:
                n_str = str(total)
                seen.add(total)
                total = 0
        
        return False
