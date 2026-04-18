class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []
        
        for item in s:
            if item in '[({':
                stack.append(item)
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if pairs[item] != pair:
                    return False

        return len(stack) == 0
