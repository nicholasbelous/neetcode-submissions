class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        prev_lower = None
        sol_found = set()
        for x in range(len(nums)-2):
            if(nums[x] == prev_lower):
                continue
            prev_lower = nums[x]
            val_dict = {}

            for n in range(x+1, len(nums)):
                if nums[n] in val_dict and nums[n] not in sol_found:
                    sol.append([val_dict[nums[n]][0], val_dict[nums[n]][1], nums[n]])
                    sol_found.add(nums[n])
                prev = nums[n]
                val_dict[(nums[n] + nums[x]) * -1] = [nums[n], nums[x]]

            

        return sol