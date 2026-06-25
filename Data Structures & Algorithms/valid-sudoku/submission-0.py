class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Checking The Rows

        rowSet = set()
        rowList = []

        for row in board:
            rowSet = set()
            rowList = []
            for val in row:
                if(val == "."):
                    pass
                else:
                    rowSet.add(val)
                    rowList.append(val)
            if(len(rowSet) != len(rowList)):
                return False
        

        for col in range(8):
            colSet = set()
            colList = []
            for row in range(8):
                if(board[col][row]):
                    pass
                else:
                    rowSet.add(board[col][row])
                    rowList.append(board[col][row])
            if(len(rowSet) != len(rowList)):
                return False

        return True
            
                