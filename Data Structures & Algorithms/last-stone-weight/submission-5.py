import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return stones[0]
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)


        while len(max_heap) > 1:
            x = (heapq.heappop(max_heap)) * -1
            y = (heapq.heappop(max_heap)) * -1

            if x == y:
                continue
            elif x > y:
                heapq.heappush(max_heap, -(x-y))
            else:
                heapq.heappush(max_heap, -(y-x))

        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0