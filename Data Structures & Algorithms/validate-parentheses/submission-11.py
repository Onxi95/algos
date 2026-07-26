class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for bracket in s:
            if bracket in ')}]':
                if not stack:
                    return False
                possible = stack.pop()

                if pairs[possible] != bracket:
                    return False
                
            else:
                stack.append(bracket)

        return len(stack) == 0