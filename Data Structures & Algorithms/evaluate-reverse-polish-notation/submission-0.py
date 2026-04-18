class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '*/+-':
                if len(stack) < 2:
                    return False
                first = stack.pop()
                second = stack.pop()
                if token == '*':
                    stack.append(first * second)
                elif token == '/':
                    stack.append(int(second / first))
                elif token == '-':
                    stack.append(int(second - first))
                else:
                    stack.append(second + first)
            else:
                stack.append(int(token))
        
        return stack[0]