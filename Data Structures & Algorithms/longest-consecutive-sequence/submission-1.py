class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 1


        for num in nums:
            if((num - 1) in numSet):
                curNum = num
                counter = 1
                while(curNum in numSet):
                    counter += 1
                    curNum += 1
                
                if(counter > longest):
                    longest = counter

        return longest
