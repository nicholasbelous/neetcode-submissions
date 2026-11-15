from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = []
        for w in range(len(strs)):
            sorted_words.append("".join(sorted(strs[w])))

        wrd_dict = defaultdict(list)

        for w in range(len(sorted_words)):
            wrd_dict[sorted_words[w]].append(strs[w])
        
        res = []

        for v in wrd_dict.values():
            res.append(v)

        return res

