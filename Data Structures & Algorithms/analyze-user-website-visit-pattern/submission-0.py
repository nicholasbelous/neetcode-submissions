from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        pattern_counts = defaultdict(int)

        for visit in range(len(username)):
            user_visits[username[visit]].append(website[visit])

        for v in user_visits.values():
            if len(v) < 3:
                continue

            l, r = 0, 3

            while r <= len(v):
                pattern_counts[tuple(v[l:r])] += 1
                l += 1
                r += 1
        
        cur_best = []
        for k, v in pattern_counts.items():
            if cur_best == []:
                cur_best = [k, v]
                continue
            
            if v < cur_best[1]:
                continue
            elif v == cur_best[1]:
                if k < cur_best[0]:
                    cur_best[0] = k
            else:
                cur_best = [k,v]



        return list(cur_best[0])
