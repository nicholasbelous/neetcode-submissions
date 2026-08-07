class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        

        def isPrefixAndSuffix(str1, str2):
            length = len(str1)

            if(len(str2) < len(str1)):
                return False

            return str2[0:length] == str1 and str2[len(str2)-length:] == str1

        left, right = 0, 1
        counter = 0
        while left < len(words) - 1:
            if(isPrefixAndSuffix(words[left], words[right])): 
                counter += 1
            if(right == len(words) - 1):
                left += 1
                right = left + 1
            else:
                right += 1

        return counter