class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        seen = set()
        for num in range(len(nums)):
            numMap[num] = set()

        for n in nums:
            counter = 1
            if(n in seen):
                while(n not in numMap[counter]):
                    counter += 1
                numMap[counter].remove(n)
                numMap[counter + 1].add(n)

            else:
                numMap[1].add(n)

        
        finalLis = []

        for n in range(len(nums) -1, 0, -1):
            if(len(finalLis) == k):
                break
            
            if (len(numMap[n]) != 0):
                finalLis.append(numMap[n].pop())

        return finalLis


                