from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        best_len = 0
        best_start = 0
        left = 0

        for right in range(len(s)):
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1

            while missing == 0:
                if best_len == 0 or right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return s[best_start:best_start + best_len] if best_len else ""