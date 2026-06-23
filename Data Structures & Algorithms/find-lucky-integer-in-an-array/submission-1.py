class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = {}

        for n in arr:
            if(n in nums):
                nums[n] += 1
            else:
                nums[n] = 1
            

        largest = -1

        for key, value in nums.items():
            if(key == value):
                largest = max(key, largest)


        return largest