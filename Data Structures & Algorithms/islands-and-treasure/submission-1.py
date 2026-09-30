from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while queue:
            row, col = queue.popleft()

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    queue.append((nr, nc))