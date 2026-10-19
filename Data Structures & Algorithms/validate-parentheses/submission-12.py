class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        assoc = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                expected = assoc[char]
                if last != expected:
                    return False

        return len(stack) == 0