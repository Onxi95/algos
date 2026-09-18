class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        expected = [0 for x in range(1, len(grid)** 2 + 1)]

        for col in range(len(grid)):
            for row in range(len(grid)):
                val = grid[col][row]
                expected[val - 1] += 1
        
        repeated, missing = 0, 0
        for index, num in enumerate(expected):
            if num > 1:
                repeated = index + 1
            elif num == 0:
                missing = index + 1

        return [repeated, missing]