class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        current_area = min(heights[left], heights[right]) * (right - left)

        while left < right:
            left_bar = heights[left]
            right_bar = heights[right]
            inner_area = min(heights[left], heights[right]) * (right - left)
            current_area = max(inner_area, current_area)

            if left_bar < right_bar:
                left += 1
            else:
                right -= 1
            
        return current_area