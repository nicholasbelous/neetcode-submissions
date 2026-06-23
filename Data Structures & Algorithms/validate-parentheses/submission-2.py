class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open = ['[', '{', '(']
        close = [']', '}', ')']

        for char in s:
            if char in open:
                stack.append(char)
            else:
                if (len(stack) == 0 or stack.pop() != open[close.index(char)]):
                    return False

        if len(stack) == 0:
            return True
        return False
