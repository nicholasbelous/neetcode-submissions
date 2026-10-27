class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        l = 0
        r = len(nums)
        mid = r // 2

        l_max = float('-inf')
        cur_l = 0

        for n in range(mid, -1, -1):
            cur_l += nums[n]
            l_max = max(l_max, cur_l)

        r_max = float('-inf')
        cur_r = 0
        for n in range(mid, r):
            cur_r += nums[n]
            r_max = max(l_max, cur_l)

        return max(l_max, r_max, l_max + r_max)

