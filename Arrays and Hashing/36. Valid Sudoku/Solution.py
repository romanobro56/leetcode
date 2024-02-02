class Solution(object):
    def isValidSudoku(self, board):
        squares = collections.defaultdict(set)
        for j in range(9):
            row = set()
            col = set()
            for i in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j] != ".":
                    row.add(board[i][j])
                if board[j][i] in col:
                    return False
                elif board[j][i] != ".": 
                    col.add(board[j][i])
        
                if board[i][j] in squares[(i//3, j//3)]:
                    return False
                elif board[i][j] != ".":
                    squares[(i//3), (j//3)].add(board[i][j])
        return True
            
