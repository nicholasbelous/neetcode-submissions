class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        highest_count = 0

        for n in num_set:
            if n - 1 not in num_set:
                count = 1

                while n + count in num_set:
                    count += 1

                highest_count = max(highest_count, count)

        return highest_count