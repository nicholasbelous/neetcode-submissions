from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # I want to keep a monotonic stack
        # so 30 -> 38 works then when adding 30 -> I pop 30 and 38


        solution = [0] * len(temperatures) 
        mono_stack = deque()

        for i, t in enumerate(temperatures):
            while mono_stack and t > mono_stack[-1][0]:
                stackT, stackInd = mono_stack.pop()
                solution[stackInd] = i - stackInd
            mono_stack.append((t, i))
        return solution



        