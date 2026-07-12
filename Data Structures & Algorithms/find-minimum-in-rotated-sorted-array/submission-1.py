class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left < right:
            mid = (right + left) // 2 

            if(nums[mid] < nums[right] and nums[mid] > nums[left]):
                return nums[left]
            elif(nums[left] > nums[right] and nums[left] < nums[mid]):
                left = mid
            else:
                right = mid

        return nums[right]