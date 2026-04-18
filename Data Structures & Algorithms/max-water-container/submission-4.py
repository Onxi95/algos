class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total_max = 0

        while left < right:
            height_l = heights[left]
            height_r = heights[right]

            current_max = (right - left) * min(height_l, height_r)
            total_max = max(current_max, total_max)

            if height_l < height_r:
                left += 1
            else:
                right -= 1

        return total_max