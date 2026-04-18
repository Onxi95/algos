class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def search(row: int, col: int) -> None:
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    a,b = r + dr, c + dc
                    if a in range(rows) and b in range(cols) and grid[a][b] == "1" and (a,b) not in visited:
                        queue.append((a,b))
                        visited.add((a,b))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    search(row, col)
                    islands += 1
        
        return islands