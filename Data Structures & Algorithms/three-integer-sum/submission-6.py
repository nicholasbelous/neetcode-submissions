class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        prev_lower = None
        for x in range(len(nums)-2):
            if(nums[x] == prev_lower):
                continue
            prev_lower = nums[x]
            val_dict = {}
            # prev = None

            for n in range(x, len(nums)-2):
                if nums[n] in val_dict:
                    sol.append([val_dict[nums[n]][0], val_dict[nums[n]][1], nums[n]])
                prev = nums[n]
                val_dict[(nums[n] + nums[x]) * -1] = [nums[n], nums[x]]

            

        return sol