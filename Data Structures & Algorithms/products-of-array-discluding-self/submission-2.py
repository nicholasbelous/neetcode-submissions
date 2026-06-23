class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1

        hasZero = 0
        
        for n in nums:
            if (n == 0):
                hasZero += 1
            else:
                total *= n
        
        for n in range(len(nums)):
            curVal = nums[n]
            if(hasZero >= 2):
                nums[n] = 0;
            elif(hasZero == 1):
                if nums[n] == 0:
                    nums[n] = total
                else:
                    nums[n] = 0
            else:
                nums[n] = int(total / curVal)

        return nums