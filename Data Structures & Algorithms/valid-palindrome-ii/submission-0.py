class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        deleteUsed = False


        while left < right:
            if(s[left] == s[right]):
                left += 1
                right -= 1
            else:
                if deleteUsed == False:
                    deleteUsed = True
                    if (s[right - 1]) == s[left]:
                        right -= 1
                    else:
                        left += 1 
                else:
                    return False
                

        return True
