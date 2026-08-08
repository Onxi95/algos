class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []

        for index, height in enumerate(heights):
            start_idx = index
            while stack and stack[-1][1] > height:
                prev_idx, prev_height = stack.pop()
                result = max(result, prev_height * (index - prev_idx))
                start_idx = prev_idx
            
            stack.append((start_idx, height))

        for index, height in stack:
            result = max(result, height * (len(heights) - index))

        return result