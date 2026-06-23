class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultingClusters = []
        seenStrings = []
        for s in strs:
            sortedStr = "".join(sorted(s))
            if(sortedStr in seenStrings):
                index = seenStrings.index(sortedStr)
                resultingClusters[index].append(s)
            else:
                seenStrings.append(sortedStr)
                resultingClusters.append([s])
        return resultingClusters

        