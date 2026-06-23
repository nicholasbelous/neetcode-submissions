class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0 , len(heights)-1

        area = 0

        while start < end:
            length = end - start
            height = min(heights[start], heights[end])

            tempArea = length * height

            area = max(area, tempArea)

            if(heights[start] > heights[end]):
                end -= 1
                continue
            else:
                start += 1

        return area