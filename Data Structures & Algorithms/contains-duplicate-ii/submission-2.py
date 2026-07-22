class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(len(nums) <= 1):
            return False

        left, right = 0 , 0
        
        while left < len(nums) - 1:
            if(right == (len(nums) - 1)):
                left += 1
            elif(left == right):
                right += 1

            dif = right - left

            while(dif <= k):
                if(right == len(nums)):
                    break
                if(nums[left] == nums[right]):
                    return True
                    
                right += 1
                dif = right - left

            left += 1
            right = left + 1

        return False