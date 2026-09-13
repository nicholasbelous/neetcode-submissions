from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_val = len(nums) // 2
        num_counts = Counter(nums)

        for k,v in majority_val.items():
            if v > mavority_val:
                return k

        return None