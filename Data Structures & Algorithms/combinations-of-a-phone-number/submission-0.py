class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        memory = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index: int, part: List[str]):
            if index >= len(digits):
                result.append("".join(part))
                return
            
            current = digits[index]
            for letter in memory[current]:
                backtrack(index + 1, part + [letter])
            
        backtrack(0, [])

        return result