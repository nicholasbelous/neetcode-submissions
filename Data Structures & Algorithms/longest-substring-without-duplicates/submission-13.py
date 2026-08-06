class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        cur = ""

        while right < len(s):
            while s[right] in cur:
                left += 1
                cur = cur[1:]
            
            cur = cur + s[right]
            right += 1
            longest = max(longest, len(cur))


        return longest