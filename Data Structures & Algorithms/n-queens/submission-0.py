class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        current = [["."] * n for j in range(n)]

        def backtrack(x: int):
            if n == x:
                inner = ["".join(row) for row in current]
                result.append(inner)
                return

            for y in range(n):
                if isSafe(current, x, y):
                    current[y][x] = "Q"
                    backtrack(x + 1)
                    current[y][x] = "."
                        
        def isSafe(board: List[List[int]], x: int, y: int) -> bool:
            if not (0 <= x < len(board)) or not (0 <= y < len(board)):
                return False

            # check current row:
            for cell in range(len(board[0])):
                if board[y][cell] == "Q":
                    return False

            # check column:
            for i in range(len(board[0])):
                if board[i][x] == "Q":
                    return False

            # check diagonals
            row, col = y -1, x - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = y + 1, x - 1
            while row < n and col >= 0:
                if board[row][col] == "Q":
                    return False
                row += 1
                col -= 1

            return True


        backtrack(0)

        return result