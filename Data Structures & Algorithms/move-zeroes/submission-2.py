class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, 0 

        while r < len(nums) and l < len(nums):
            if nums[l] != 0:
                l += 1
            else:
                r = l
                while r < len(nums) and nums[r] == 0:
                    r += 1
                if r == len(nums):
                    return None
                nums[l] = nums[r]
                nums[r] = 0

                l += 1
        