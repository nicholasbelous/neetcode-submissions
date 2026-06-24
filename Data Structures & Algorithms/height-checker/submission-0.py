class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        counter = 0

        for n in range(len(heights)):
            if(expected[n] != heights[n]):
                counter += 1

        return counter