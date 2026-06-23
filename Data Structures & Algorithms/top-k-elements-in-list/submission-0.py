class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCounts = {}
        bucketList = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if(num in numberCounts):
                numberCounts[num] += 1
            else:
                numberCounts[num] = 1

        for num , freq in numberCounts.items():
            bucketList[freq].append(num)

        returnList = []
        while(len(returnList) != k):
            if(len(bucketList[-1]) == 0):
                bucketList.pop()
            else:
                returnList.append(bucketList[-1].pop())

        return returnList