class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        width = len(matrix[0])

        while top <= bottom:
            mid_vertical = (top + bottom) // 2
            if matrix[mid_vertical][0] <= target <= matrix[mid_vertical][-1]:
                return self.binary_search(matrix[mid_vertical], target)
            elif target < matrix[mid_vertical][0]:
                bottom = mid_vertical - 1
            else:
                top = mid_vertical + 1

        return False

    def binary_search(self, matrix: List[int], target: int):
        left = 0
        right = len(matrix)

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        return False