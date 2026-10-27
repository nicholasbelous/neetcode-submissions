class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Base Case: Only one element
        if len(nums) == 1:
            return nums[0]
            
        mid = len(nums) // 2
        
        # 1. Recursively find the max subarray in the left and right halves
        left_max = self.maxSubArray(nums[:mid])
        right_max = self.maxSubArray(nums[mid:])
        
        # 2. Find the max subarray crossing the middle (Your logic, fixed)
        l_max = float('-inf')
        cur_l = 0
        for n in range(mid - 1, -1, -1):
            cur_l += nums[n]
            l_max = max(l_max, cur_l)

        r_max = float('-inf')
        cur_r = 0
        for n in range(mid, len(nums)):
            cur_r += nums[n]
            r_max = max(r_max, cur_r)
            
        cross_max = l_max + r_max
        
        # 3. Return the absolute best of the three options
        return max(left_max, right_max, cross_max)
