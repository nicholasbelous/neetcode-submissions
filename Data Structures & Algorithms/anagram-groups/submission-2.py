from collections import defaultdict, Counter 
from types import MappingProxyType 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            groups[frozenset(Counter(s))].append(s)
        
        final_lis = []

        for v in groups.values():
            final_lis.append(v)

        return final_lis
