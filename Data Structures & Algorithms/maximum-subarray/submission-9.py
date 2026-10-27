class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_sum = nums[0]
        
        for n in nums[1:]:
            # Either start a new subarray at 'n' or add 'n' to the current one
            current_sum = max(n, current_sum + n)
            max_so_far = max(max_so_far, current_sum)
            
        return max_so_far
