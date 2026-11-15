class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        
        mem = [0] * len(nums)
        mem[0] = max(nums[0], 0)
        mem[1] = max(mem[0], nums[1])

        for n in range(2, len(nums)):
            mem[n] = max(mem[n-2] + nums[n], mem[n-1])
        
        print(mem)
        return mem[-1]


        