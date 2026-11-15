class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_i = sorted(intervals, key=lambda x: x[0])

        sol = []

        for n in sorted_i:
            if len(sol) == 0:
                sol.append(n)
            
            if sol[-1][1] >= n[0]:
                sol[-1][1] = n[1]
            else:
                sol.append(n)

        return sol


