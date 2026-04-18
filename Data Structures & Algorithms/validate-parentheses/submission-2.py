class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                candidate = stack.pop()
                if mapping[candidate] != char:
                    return False

        return len(stack) == 0