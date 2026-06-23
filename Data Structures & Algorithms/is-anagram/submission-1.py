class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDic = {}
        tDic = {}

        for num in range(len(s)):
            if(s[num] in sDic):
                sDic[s[num]] += 1
            else: 
                sDic[s[num]] = 1

            if(t[num] in tDic):
                tDic[t[num]] += 1
            else: 
                tDic[t[num]] = 1

        return sDic == tDic