class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0

        long = 1
        left, right = 0, 1

        curSeq = [s[0]]

        while right < len(s):
            if(len(curSeq) == len(set(curSeq))):
                long = max(long, len(curSeq))
                curSeq.append(s[right])
                right += 1
            else:
                curSeq.pop(0)
                left += 1

        long = max(long, len(set(curSeq)))
        return long