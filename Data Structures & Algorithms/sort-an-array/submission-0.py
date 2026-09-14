class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        sorted = False 


        while sorted is False:
            sorted = True
            
            for index in range(len(nums) - 1):
                if(nums[index] > nums[index + 1]):
                    sorted = False
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]
        
        return nums