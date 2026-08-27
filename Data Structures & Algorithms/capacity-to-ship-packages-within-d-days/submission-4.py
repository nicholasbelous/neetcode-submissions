class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            max_w = (lo + hi) // 2

            total_w = 0
            day = 1

            for w in weights:
                if total_w + w > max_w:
                    day += 1
                    total_w = 0
                total_w += w

            if day <= days:
                hi = max_w
            else:
                lo = max_w + 1

        return lo