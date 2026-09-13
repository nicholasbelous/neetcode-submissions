from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_val = len(nums) // 2
        num_counts = Counter(nums)

        for k,v in num_counts.items():
            if v > majority_val:
                return k

        return None