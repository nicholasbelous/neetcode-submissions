class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        # prev_lower = None

        for x in range(len(nums)):
            # if(nums[x] == prev_lower):
            #     continue
            # prev_lower = nums[x]

            val_dict = {}

            for n in range(x+1, len(nums)):
                if nums[n] in val_dict:
                    sol.add((val_dict[nums[n]][0], val_dict[nums[n]][1], nums[n]))
                    # sol_found.add(nums[n])
                prev = nums[n]
                val_dict[(nums[n] + nums[x]) * -1] = [nums[n], nums[x]]

            

        return [list(t) for t in sol]