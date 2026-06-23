class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sLetters = {}
        tLetters = {}

        for l in s:
            if(l in sLetters):
                sLetters[l] += 1
            else:
                sLetters[l] = 1

        for l in t:
            if(l in tLetters):
                tLetters[l] += 1
            else:
                tLetters[l] = 1

        return sLetters == tLetters