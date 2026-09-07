class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        
        if(k == 0):
            return None

        left = 0
        right = len(nums) - 1
        while left <= right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1

        left = 0
        right = k - 1
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1

        left = k
        right = len(nums) - 1
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1
        return None

        