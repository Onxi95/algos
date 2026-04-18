class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0

        max_l = [0] * len(height)
        max_r = [0] * len(height)

        max_l[0] = height[0]
        for i in range(1, len(height)):
            max_l[i] = max(height[i], max_l[i - 1])

        max_r[-1] = height[len(height) - 1]
        for i in range(len(height) -2, -1, -1):
            max_r[i] = max(height[i],max_r[i + 1])


        result = 0

        for i in range(len(height)):
            min_arr = min(max_l[i], max_r[i])
            result += min_arr - height[i]

        return result