class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for l in s:
            if l in ["(", "[", "{"]:
                stack.append(l)
            else:
                if(len(stack) == 0):
                    return False
                if(l == ")" and stack[-1] == "("):
                    stack.pop()
                elif(l == "]" and stack[-1] == "["):
                    stack.pop()
                elif(l == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False



        return len(stack) == 0