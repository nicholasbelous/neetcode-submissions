class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        seen = set()

        highest_count = 0

        for n in nums:
            if n not in seen:
                count = 1
                seen.add(n)

                while n + 1 in set_nums:
                    count += 1
                    seen.add(n+1)
                    n += 1
            
                highest_count = max(highest_count, count)

        return highest_count
        