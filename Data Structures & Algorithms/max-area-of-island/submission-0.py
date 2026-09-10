class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        total = 0
        if not grid:
            return total

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 0
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            
            current = 1
            for dr, dc in dirs:
                current += dfs(row + dr, col + dc)

            return current            

        for row in range(ROWS):
            for col in range(COLS):
                current = 0
                if grid[row][col] == 1:
                    current = dfs(row, col)
                total = max(total, current)


        return total
