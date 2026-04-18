class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        stack = []

        def backtracking(open_n: int, close_n: int) -> None:
            if open_n == close_n == n:
                result.append("".join(stack))
                return
            if open_n < n:
                stack.append('(')
                backtracking(open_n + 1, close_n)
                stack.pop()
            if close_n < open_n:
                stack.append(')')
                backtracking(open_n, close_n + 1)
                stack.pop()

        backtracking(0, 0)

        return result