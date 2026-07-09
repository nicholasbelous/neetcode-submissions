class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if(len(s) == 1):
            return 1
        
        L = 0

        counts = {}
        longest = 0

        for R in range(len(s)):
            if(s[R] in counts):
                counts[s[R]] += 1
            else: 
                counts[s[R]] = 1

            maxFreq = max(counts.values())

            while (R - L + 1) - maxFreq > k:
                counts[s[L]] -= 1
                L += 1
                maxFreq = max(counts.values())

            longest = max(longest, R - L + 1)

        return longest

