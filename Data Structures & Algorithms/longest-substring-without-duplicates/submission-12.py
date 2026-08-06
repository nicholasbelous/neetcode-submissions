class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        cur = ""

        while right < len(s):
            if(len(set(cur)) != len(cur)):
                left += 1
                cur = cur[1:]
            else:
                longest = max(longest, len(cur))
                cur = cur + s[right]
                right += 1

        if(len(set(cur)) == len(cur)):
            longest = max(longest, len(cur))

        return longest