from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                current = board[row][col]
                
                if current in rows[row] or current in cols[col] or current in squares[(row // 3, col // 3)]:
                    return False
                
                cols[col].add(current)
                rows[row].add(current)
                squares[(row // 3, col // 3)].add(current)

        return True