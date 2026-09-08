class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def backtrack(left: int, right: int):
            if left == right == n:
                result.append("".join(current))
                return
            
            if left < n:
                current.append("(")
                backtrack(left + 1, right)
                current.pop()

            if right < left:
                current.append(")")
                backtrack(left, right + 1)
                current.pop()

        backtrack(0, 0)

        return result