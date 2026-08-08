class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if(len(matrix) == 0):
            return

        top, bot = 0, len(matrix) -1
        while top < bot:
            matrix[bot], matrix[top] = matrix[top], matrix[bot]
            top +=1
            bot -=1
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
