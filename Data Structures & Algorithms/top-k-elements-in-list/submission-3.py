import heapq
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = Counter(nums)
        
        k_common = num_dict.most_common(k)

        common_arr = []

        for tup in k_common:
            common_arr.append(tup[0])

        return common_arr

