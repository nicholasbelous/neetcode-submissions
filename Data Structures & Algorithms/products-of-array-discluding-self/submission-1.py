class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1

        hasZero = 0
        
        for n in nums:
            if (n == 0):
                hasZero += 1
            else:
                total *= n

        resList = []
        
        for n in nums:
            if(hasZero >= 2):
                resList.append(0)
            elif(hasZero == 1):
                if n == 0:
                    resList.append(total)
                else:
                    resList.append(0)
            else:
                resList.append(int(total / n))

        return resList