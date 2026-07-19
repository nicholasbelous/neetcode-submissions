class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""

        for _ in range(len(strs[0])):
            letterSet = set()

            for n in range(len(strs)):
                if(len(strs[n]) == 0):
                    return pref

                letterSet.add(strs[n][0])
                strs[n] = strs[n][1:]

            if(len(letterSet) == 1):
                pref += letterSet.pop()
            else:
                return pref
            
        return pref



