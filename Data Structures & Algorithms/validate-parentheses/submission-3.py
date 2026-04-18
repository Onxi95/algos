class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []
        
        for item in s:
            if item in pairs.values():
                stack.append(item)
            else:
                if not stack:
                    return False
                potential_pair = stack.pop()
                if potential_pair != pairs[item]:
                    return False

        return len(stack) == 0