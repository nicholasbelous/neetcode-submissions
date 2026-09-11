from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_window = ""
        t_counts = Counter(t)
        window_counts = Counter()
        left = 0

        for r in range(len(s)):
            window_counts[s[r]] += 1

            while t_counts <= window_counts:
                current_window = s[left:r + 1]
                if best_window == "" or len(current_window) < len(best_window):
                    best_window = current_window
                window_counts[s[left]] -= 1
                left += 1

        return best_window