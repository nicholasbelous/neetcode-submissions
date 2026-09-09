class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        max_area = 0
        
        while left < right:
            area = (right - left) * min(nums[right], nums[left])
            
            max_area = max(area, max_area)
            
            if(nums[right] < nums[left]):
                right -= 1
            elif(nums[right] > nums[left]):
                left += 1
            else:
                if(nums[left+1] > nums[right-1]):
                    left += 1
                else:
                    right -= 1
                    
        return max_area