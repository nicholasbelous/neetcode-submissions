class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        wordLen = []



        for l in range(len(s) -1, 0, -1):
            if(s[l] == " " and len(word) == 0):
                return len(word)
            elif(s[l] == " "):
                continue
            else:
                word += s[l]

        return None