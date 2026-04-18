from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                current = board[row][col]
                if current == '.':
                    continue
                if current in rows[row] or current in cols[col]:
                    return False
                if  current in squares[(row // 3, col // 3)]:
                    return False
                cols[col].add(current)
                rows[row].add(current)
                squares[(row // 3, col // 3)].add(current)

        return True