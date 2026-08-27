from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for n in range(len(nums)):
            if nums[n] in d:
                return [d[nums[n]], n]
            else:
                d[target - nums[n]] = n
        
        return None
            



