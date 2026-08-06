class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        cur = ""

        while left < len(s):
            if(len(set(cur)) != len(cur)):
                left += 1
                cur = cur[1:-1]
            else:
                longest = max(longest, len(cur))
                right += 1
                if(right == len(s)):
                    break
                cur = cur + s[right]
        if(len(set(cur)) != len(cur)):
            longest = max(longest, len(cur))

        return longest