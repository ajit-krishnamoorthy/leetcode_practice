#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the rules
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in square[(r//3, c//3)]):
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True