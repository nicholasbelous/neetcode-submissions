from collections import defaultdict, Counter 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            groups[tuple(sorted(Counter(s)))].append(s)
        
        final_lis = []

        for v in groups.values():
            final_lis.append(v)

        return final_lis
