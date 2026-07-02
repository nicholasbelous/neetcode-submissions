class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        sCount = {}
        tCount = {}

        for n in range(len(s)):
            if(s[n] in sCount):
                sCount[s[n]] += 1
            else:
                sCount[s[n]] = 1
            
            if(t[n] in tCount):
                tCount[t[n]] += 1
            else:
                tCount[t[n]] = 1
        
        return sCount == tCount