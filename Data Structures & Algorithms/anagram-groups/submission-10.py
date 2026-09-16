from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = []
        for w in strs:
            sorted_words.append("".join(sorted(w)))

        sorted_word_groups = defaultdict(list)
        
        for index, value in enumerate(sorted_words):
            sorted_word_groups[value].append(strs[index])
        
        
        final_list = []
        for v in sorted_word_groups.values():
            final_list.append(v)


        return final_list