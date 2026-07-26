class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        postfix = [0] * n
        result = [0] * n

        prefix[0] = height[0]
        postfix[-1] = height[-1]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            postfix[i] = max(postfix[i + 1], height[i])

        for i in range(n):
            result[i] = min(prefix[i], postfix[i]) - height[i]

        return sum(result)