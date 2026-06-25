class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numStreakCount = {}
        
        for num in nums:
            if(num - 1 in numStreakCount):
                numStreakCount[num] = numStreakCount[num-1]