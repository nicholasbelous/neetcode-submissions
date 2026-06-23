class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        while(len(nums) > 1):
            middle = len(nums) // 2

            upper = nums[middle : ]
            lower = nums[ : middle]


            if(nums[middle] == target):
                index += middle
                return index
            elif(nums[middle] > target):
                nums = lower
            else:
                nums = upper
                index += middle
        
        if(nums[0] == target):
            return index
            
        return -1