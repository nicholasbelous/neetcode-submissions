class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(len(nums) <= 1):
            return False

        left, right = 0 , 0
        
        while left < len(nums) - 2:
            if(right == (len(nums) - 1)):
                left += 1
            if(left == right):
                right += 1

            if((right - left) <= k):
                if(nums[left] == nums[right]):
                    return True
                else:
                    right += 1
                    
            left += 1

        return False