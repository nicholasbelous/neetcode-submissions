class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open = ['[', '{', '(']
        close = [')', '}', ']']

        for char in s:
            if char in open:
                stack.append(char)
            
            if(len(stack) != 0 and stack.pop() != char):
                return false
        return True