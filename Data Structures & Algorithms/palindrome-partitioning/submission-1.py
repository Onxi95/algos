class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s: str):
            return s == s[::-1]

        def backtrack(index: int, current: List[str]):
            if index >= len(s):
                result.append(current[:])
                return

            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]
                if isPalindrome(substring):
                    current.append(substring)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])

        return result