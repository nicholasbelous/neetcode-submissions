class Solution:
    def isPalindrome(self, s: str) -> bool:
        simpleString = "".join(filter(str.isalnum, s)).lower()
        strLength = len(simpleString)
        for n in range(strLength // 2):
            if(simpleString[n] != simpleString[strLength - 1 - n]):
                return False
        
        # If No problems are found we are good to return false
        return True
        