class Solution:
    #        5
    #    -1=4  -2 =3
    #   -1=3
    #  -1=2
    # -1=1
    #-1=0
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n: int):
            if n in memo:
                return memo[n]

            if n < 0:
                return 0
            if n == 0:
                return 1

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
        return dfs(n)