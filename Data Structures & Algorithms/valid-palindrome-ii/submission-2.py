class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        deleteUsed = False
        firstCheck = False
        lHold, rHold = 0, 0

        while left < right:
            if(s[left] == s[right]):
                left += 1
                right -= 1
            else:
                if deleteUsed == False:
                    deleteUsed = True
                    lHold, rHold = left, right
                    right -= 1
                elif(deleteUsed == False and firstCheck == False):
                    firstCheck = True
                    left = lHold + 1
                    right = rHold
                else:
                    return False
                

        return True
