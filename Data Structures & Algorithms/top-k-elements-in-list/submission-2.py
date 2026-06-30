class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        seen = set()

        for num in range(len(nums) + 1):
            numMap[num] = set()

        for n in nums:
            if(n in seen):
                counter = 1
                while(n not in numMap[counter]):
                    counter += 1
                numMap[counter].remove(n)
                numMap[counter + 1].add(n)

            else:
                numMap[1].add(n)
                seen.add(n)

        
        finalLis = []

        for n in range(len(nums), 0, -1):
            while(len(numMap[n]) != 0):
                if (len(finalLis) == k):
                    break
                finalLis.append(numMap[n].pop())

            if (len(finalLis) == k):
                break

        return finalLis


                