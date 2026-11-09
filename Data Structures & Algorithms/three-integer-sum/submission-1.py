from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        end = len(nums)
        nums = sorted(nums)

        for static in range(end):
            sum_dict = defaultdict(list)

            if static > 0 and nums[static] == nums[static-1]:
                continue
            for n in range(static + 1, end, 1):
                if(static >= end - 2):
                    break
                if(nums[n] in sum_dict):
                    print(sum_dict)
                    print(static)
                    print([nums[n]] + sum_dict[nums[n]])
                    output.append([nums[n]] + sum_dict[nums[n]])
                total = nums[static] + nums[n]
                total = total * (-1)

                sum_dict[total] = [nums[static], nums[n]]
            sum_dict.clear()

        return output

