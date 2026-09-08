class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(reminder: int):
            nonlocal result, memo
            if reminder == 0:
                return 0
            if reminder < 0:
                return float('inf')

            if reminder in memo:
                return memo[reminder]

            winner = float('inf')

            for coin in coins:
                res = dfs(reminder - coin)
                winner = min(winner, res + 1)
            memo[reminder] = winner
            return winner
            
        result = dfs(amount)
        return result if result != float('inf') else -1