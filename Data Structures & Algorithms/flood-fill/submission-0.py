class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        result = [[col for col in row] for row in image]
        ROWS = len(image)
        COLS = len(image[0])
        original_color = image[sr][sc]

        def dfs(row: int, col: int, visited):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            if (row, col) in visited:
                return
            if image[row][col] != original_color:
                return

            result[row][col] = color

            visited.add((row, col))
            dfs(row + 1, col, visited)
            dfs(row -1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)

            visited.remove((row, col))

        dfs(sr, sc, set())

        return result