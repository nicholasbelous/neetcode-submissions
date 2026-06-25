class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if(not heights):
            return 0
        
        maxVol = 0
        left , right = 0, len(heights) - 1 


        while left < right:
            
            height = min(heights[left], heights[right])
            length = right - left

            area = length * height
            maxVol = max(area, maxVol)

            left += 1


        return maxVol