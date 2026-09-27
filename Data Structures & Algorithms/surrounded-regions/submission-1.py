class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def mark_border(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            if board[row][col] != "O":
                return
            board[row][col] = "#"
            for dx, dy in dirs:
                mark_border(row + dx, col + dy)

        for row in range(ROWS):
            for col in range(COLS):
                if (row in (0, ROWS - 1) or col in (0, COLS - 1)) and board[row][col] == "O":
                    mark_border(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"