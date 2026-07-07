class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while(left <= right):
            mid = (left + right) // 2

            if(nums[mid] == target):
                return mid

            if(nums[left] <= nums[mid]):
                #left half of the list is sorted
                if(target > nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    if(left == mid):
                        break
                    left = mid
            else:
                #right half of the list is sorted
                if(target > nums[mid] and target < nums[right]):
                    left = mid + 1
                else:
                    if(right == mid):
                        break
                    right = mid

        return -1