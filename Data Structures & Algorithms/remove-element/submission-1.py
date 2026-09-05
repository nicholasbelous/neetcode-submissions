class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0 

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                k += 1
            elif nums[l] == val:
                r -= 1
            else:
                l += 1
                k += 1

        return k
                