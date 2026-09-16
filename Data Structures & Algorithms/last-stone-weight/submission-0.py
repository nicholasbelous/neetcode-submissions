import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            first_stone = heapq.heappop(neg_stones)
            second_stone = heapq.heappop(neg_stones)

            if(-(first_stone) > -(second_stone)):
                heapq.heappush(neg_stones, first_stone - second_stone)
            elif(-(first_stone) < -(second_stone)):
                heapq.heappush(neg_stones, second_stone - first_stone)


        if(len(neg_stones) == 1):
            return -neg_stones[0]
        else:
            return 0