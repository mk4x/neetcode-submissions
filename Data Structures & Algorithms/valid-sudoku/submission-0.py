class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                res = set()
                for x in range(i*3,i*3+3):
                    for y in range(j*3,j*3+3):
                        if board[x][y] in res:
                            #print(board[x][y], res)
                            #print("1st failed")
                            return False
                        if board[x][y] != ".":
                            res.add(board[x][y])
        
        # rows
        for i in range(9):
            res = set()
            for j in range(9):
                if board[i][j] in res:
                    #print(board[x][y], res)
                    #print("2st failed")
                    return False
                if board[i][j] != ".":
                    res.add(board[i][j])
        
        # cols
        for i in range(9):
            res = set()
            for j in range(9):
                if board[j][i] in res:
                    return False
                if board[j][i] != ".":
                    res.add(board[j][i])
        
        return True
        
        