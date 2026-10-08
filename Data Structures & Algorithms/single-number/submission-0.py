from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts = Counter(nums)

        for k, v in num_counts.items():
            if(v == 1):
                return k

        return None