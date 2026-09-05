class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return len(nums)
        
        cur_num, next_num = 0, 1


        while next_num < len(nums):
            if nums[cur_num] == nums[next_num]:
                nums.pop(next_num)
            else:
                cur_num += 1
                next_num += 1

        return len(nums) 
            
