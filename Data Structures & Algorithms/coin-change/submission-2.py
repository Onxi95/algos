class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem: int) -> int:
            if rem < 0:
                return float('inf')
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            best = float('inf')
            for c in coins:
                res = dfs(rem - c)
                if res != float('inf'):
                    best = min(best, 1 + res)

            memo[rem] = best
            return best

        min_amount = dfs(amount)

        return -1 if min_amount == float('inf') else min_amount