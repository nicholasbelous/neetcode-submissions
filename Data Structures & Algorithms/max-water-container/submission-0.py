class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if(not heights):
            return 0
        
        maxVol = 0

        arrLength = len(heights)

        for h1 in range(0, arrLength):
            for h2 in range(h1, arrLength):
                height = min(heights[h1], heights[h2])
                length = h2 - h1
                area = length * height

                maxVol = max(area, maxVol)

        return maxVol