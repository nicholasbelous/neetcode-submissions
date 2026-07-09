class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for l in s:
            stack.append(l)
        
        left, right = 0 , len(stack) - 1

        while(left < right):
            if(stack[left] == "("):
                if(stack[right] != ")"):
                    return False

            if(stack[left] == "{"):
                if(stack[right] != "}"):
                    return False

            if(stack[left] == "["):
                if(stack[right] != "]"):
                    return False
            
            left += 1
            right -= 1

        return True