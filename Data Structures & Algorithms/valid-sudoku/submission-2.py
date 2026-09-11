import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        def check_rows(board):
            seen = set()
            for row in board:
                for val in row:
                    if(val == "."):
                        continue
                    else:
                        if(val in seen):
                            return False
                        seen.add(val)
                seen = set()
            return True

        def check_cols(board):
            seen = set()
            for col in range(len(board)):
                for row in range(len(board)):
                    if(board[row][col] == "."):
                        continue
                    elif board[row][col] in seen:
                            return False
                    seen.add(board[row][col])
                seen = set()
            return True

        def check_nine(board):
            sections = []
            for r in range(0, 9, 3):
                for c in range(0, 9, 3):
                    # Correct way to slice a 2D Python list:
                    block = [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
                    sections.append(block)
            
            for section in sections:
                seen = set()
                for val in section:
                    if(val == "."):
                        continue
                    elif(val in seen):
                        return False
                    seen.add(val)
                
            return True

        return check_rows(board) and check_cols(board) and check_nine(board)