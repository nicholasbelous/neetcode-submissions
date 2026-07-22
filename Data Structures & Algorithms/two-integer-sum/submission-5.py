class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}

        for n in range (len(nums)):
            if(nums[n] in dif):
                return [dif[nums[n]], n]
            else:
                dif[target - nums[n]] = n
        
        return False