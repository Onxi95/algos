from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        clock = 0
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                current = grid[row][col]
                if current == 1:
                    fresh += 1
                elif current == 2:
                    queue.append((row, col))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in dirs:
                    new_row = dr + row
                    new_col = dc + col
                    out_of_bounds = new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS
                    if out_of_bounds or grid[new_row][new_col] != 1:
                        continue
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
                    fresh -= 1
            clock += 1
        
        return clock if fresh ==0 else - 1