class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        current_max = 0

        while left < right:
            height_l = heights[left]
            height_r = heights[right]

            area = (right - left) * min(height_l, height_r)
            current_max = max(area, current_max)

            if height_l > height_r:
                right -= 1
            else:
                left += 1

        return current_max
