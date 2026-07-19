class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""

        for letter in range(len(strs[0])):
            letterSet = set()

            for word in strs:
                letterSet.add(word[letter])

            if(len(letterSet) == 1):
                pref += letterSet.pop()
            else:
                return pref
            
        return pref



