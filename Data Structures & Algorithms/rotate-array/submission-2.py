class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        
        if(k == 0):
            return None

        left = k - 1
        right = len(nums) - 1

        if(k > len(nums) // 2):
            while left >= 0:
                nums[right], nums[left] = nums[left], nums[right]
                left -= 1
        else:

            while left >= 0:
                nums[right], nums[left] = nums[left], nums[right]
                left -= 1
                right -= 1
            
            # left = len(nums) - 2
            # right = len(nums) - 1
            # while left >= k + 1:
            #     nums[right], nums[left] = nums[left], nums[right]
            #     left -= 1
        
        print(nums)




        return None

        