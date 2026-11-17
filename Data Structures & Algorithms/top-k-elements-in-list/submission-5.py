from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        most_common = num_counts.most_common(k)

        # heap = heapq.nlargest(k, num_counts.keys(), key=num_counts.get)
        sol = []

        for e in most_common:
            sol.append(e[0])

        return sol