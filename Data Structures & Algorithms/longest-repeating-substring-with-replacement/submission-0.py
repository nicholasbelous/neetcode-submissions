class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if(len(s) == 1):
            return 1
        
        L, R = 0, 1

        longest = 0

        cur = s[L]
        counter = k

        while(R < len(s)):
            if(s[L] == s[R]):
                cur += s[R]
                R += 1
            else:
                if(counter > 0):
                    counter -= 1
                    cur += s[L]
                    R += 1
                else:
                    counter = k
                    L += 1
                    cur = s[L]
                    
            longest = max(longest, len(cur))
        
        return longest

