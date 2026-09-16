from collections import deque 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        solution_que = deque()
        
        while l <= r:
            if nums[l] < 0:
                if(-nums[l] > nums[r]):
                    solution_que.appendleft(nums[l]**2)
                    l += 1
                else:
                    solution_que.appendleft(nums[r]**2)
                    r -= 1
            else:
                solution_que.appendleft(nums[r]**2)
                r -= 1

        return list(solution_que)

