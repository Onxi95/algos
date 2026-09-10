class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        part_of_islands = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row: int, col: int, visited):
            nonlocal total
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            if (row, col) in visited:
                return
            if grid[row][col] == "0":
                return
            
            if grid[row][col] == "1":
                part_of_islands.add((row, col))

            visited.add((row, col))

            dfs(row + 1, col, visited)
            dfs(row - 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)

        total = 0

        print(len(part_of_islands))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in part_of_islands:
                    total += 1
                    dfs(r, c, set())

        return total

