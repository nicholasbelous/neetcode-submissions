class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        s_dict = {}
        t_dict = {}

        for n in range(len(s)):
            if(s[n] in s_dict):
                s_dict[s[n]] += 1
            else:
                s_dict[s[n]] = 1
    
            if(t[n] in t_dict):
                t_dict[t[n]] += 1
            else:
                t_dict[t[n]] = 1
    
        return s_dict == t_dict
