from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) < 2):
            return len(s)
        if(len(s) == 2):
            return len(set(s))

        left, right = 0, 1
        
        letter_dict = defaultdict(int)
        
        letter_dict[s[left]] += 1
        letter_dict[s[right]] += 1
        
        counter = 0
        right += 1
        while right < len(s):
            if(s[right] in letter_dict):
                while(letter_dict[s[right]] > 0):
                    letter_dict[s[left]] -= 1
                    left += 1
                letter_dict[s[right]] += 1
            else:
                letter_dict[s[right]] += 1
                
            right += 1
            counter = max(counter, sum(letter_dict.values()))
            
        return counter