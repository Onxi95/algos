class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(index: int):
            if index > len(cost) - 1:
                return 0

            if index in memo:
                return memo[index]

            left = cost[index] + dfs(index + 1)
            right = cost[index] + dfs(index + 2)

            result = min(left, right)
            memo[index] = result
            return min(left, right)

        first = dfs(0)
        second = dfs(1)

        return min(first, second)