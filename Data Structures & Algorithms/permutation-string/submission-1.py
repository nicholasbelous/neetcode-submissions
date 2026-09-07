from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        s2_counts = Counter(s2)

        if s1_counts.items() <= s2_counts.items():
            
            window_right = len(s1)
            window_left = 0
            window = s2[window_left:window_right]

            while window_right <= len(s2):
                if(Counter(window) == s1_counts):
                    return True

                window_right += 1
                window_left += 1
                window = s2[window_left:window_right]
        
        return False