class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        mid = len(nums) // 2

        while (right - left) > 1:
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid

            if target < nums[mid]:
                right = mid
            
            mid = (right + left) // 2

        if(target >= nums[right]):
            return right + 1
        else:
            return right

