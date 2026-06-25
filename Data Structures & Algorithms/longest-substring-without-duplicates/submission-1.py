class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        if(len(s) < 2):
            return len(s)
        counter = 0
        longest = 0
        for l in s:
            if(l in seen):
                seen = set()
                seen.add(l)
                if(counter > longest):
                    longest = counter
                counter = 1
            else:
                seen.add(l)
                counter += 1

        return longest
        