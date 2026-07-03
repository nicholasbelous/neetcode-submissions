class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDif = {}

        for n in range(len(nums)):
            if nums[n] in numDif:
                return [numDif[nums[n]], n]
            else:
                numDif[target - nums[n]] = n

        return None