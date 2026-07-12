class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (right + left) // 2 
            if(mid == left or mid == right):
                return min(nums[left], nums[right])

            if(nums[mid] > nums[left] and nums[left] < nums[right]):
                right = mid
            elif(nums[mid] > nums[left] and nums[left] > nums[right]):
                left = mid
            else:
                right = mid

        
        return num[left]