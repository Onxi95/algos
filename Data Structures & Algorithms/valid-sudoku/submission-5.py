class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[[] for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                current = board[row][col]
                if current == ".":
                    continue
                if current in rows[row] or current in cols[col] or current in squares[row // 3][col // 3]:
                    return False

                cols[col].append(board[row][col])
                rows[row].append(board[row][col])
                squares[row // 3][col // 3].append(board[row][col])

        return True