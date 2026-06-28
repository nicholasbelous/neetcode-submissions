class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        goodTrips = []

        sortedNums = sorted(nums)

        for n in range(len(nums)):
            if n > 0 and sortedNums[n] == sortedNums[n-1]:
                continue
            left, right = n + 1, len(nums) - 1
            while left < right:
                
                tot = sortedNums[n] + sortedNums[left] + sortedNums[right]

                if(tot == 0):
                    goodTrips.append([sortedNums[n], sortedNums[left], sortedNums[right]])
                    while left < right and sortedNums[left] == sortedNums[left + 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                elif(tot < 0):
                    left += 1
                else:
                    right -= 1
                    
        return goodTrips
        