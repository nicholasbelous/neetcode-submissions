class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if(len(s) == 1):
            return 1
        
        L, R = 0, 1

        counts = {s[L] : 1}
        longest = 1

        while(R < len(s)):
            if(s[R] in counts):
                counts[s[R]] += 1
            else: 
                counts[s[R]] = 1
            
            maxFreq = max(counts.values())
            replacements = (R - L + 1) - maxFreq
            if(replacements > k):
                counts[s[L]] -= 1
                L += 1
            else:
                longest = max(longest, R - L + 1)
                R += 1

        return longest

