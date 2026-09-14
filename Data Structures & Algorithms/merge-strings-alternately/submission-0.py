class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sort_len = min(len(word1), len(word2))
        
        new_word = ""

        for num in range(sort_len):
            new_word += word1[num]
            new_word += word2[num]

        if(len(word1) > sort_len):
            new_word += word1[sort_len:]
        elif(len(word2) > sort_len):
            new_word += word2[sort_len:]
            
        return new_word