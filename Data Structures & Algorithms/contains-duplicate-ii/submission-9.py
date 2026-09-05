class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def contains_dup(nums):
            return len(nums) != len(set(nums))
        
        
        if len(nums) < k+1: 
            return contains_dup(nums)
        
        window = []

        for n in range(k+1):
            window.append(nums[n])

        if contains_dup(window):
                return True

        for n in range(k+1, len(nums)-1):
            window.pop(0)
            window.append(nums[k])
            print(window)
            if contains_dup(window):
                return True

        return False
            

        