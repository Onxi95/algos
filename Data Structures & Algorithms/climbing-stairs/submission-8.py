class Solution:
    def climbStairs(self, n: int) -> int:
        second, last = 1, 1

        for i in range(n - 1):
            current = second + last
            second, last = current, second        

        return second