class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i in s:
            if i in pairs.values():
                stack.append(i)
            else:
                potential_pair = stack.pop() if len(stack) > 0 else 'Noop'
                if pairs[i] != potential_pair:
                    return False
        
        return len(stack) == 0