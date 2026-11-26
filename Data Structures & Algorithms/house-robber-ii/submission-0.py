class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
                return max(nums)

        def rob_linear(houses: List[int]) -> int:
            cache = [houses[0], max(houses[0], houses[1])]
            for n in range(2, len(houses)):
                next_max = max(cache[-1], cache[-2] + houses[n])
                cache.append(next_max)
            return cache[-1]

        # Compare robbing houses 0 to n-2 vs. houses 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        