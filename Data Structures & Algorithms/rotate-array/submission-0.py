class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        
        if(k == 0):
            return None

        if(k >= len(nums) // 2):
            #need to flip the right side
            left, right = len(nums) // 2, len(nums) - 1

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        else:
            #flip the left side
            left, right = 0, len(nums) // 2

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 
                right -= 1

        left, right = 0, len(nums) - 1

        while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 
                right -= 1

        #need to flip the right side
        left, right = len(nums) // 2, len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        print(nums)


        # left_pointer, right pointer = 0 , len(nums) - 1

        # for _ in range(k):

        return None

        