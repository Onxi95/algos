class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                if len(stack) < 2:
                    return -1
                first = stack.pop()
                second = stack.pop()

                if token == "+":
                    stack.append(second + first)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(second * first)
                else:
                    stack.append(int(float(second) / first))
            else:
                stack.append(int(token))
        
        return stack[0]