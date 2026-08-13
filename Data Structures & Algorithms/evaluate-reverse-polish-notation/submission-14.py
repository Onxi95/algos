class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if self.is_num(token):
                stack.append(int(token))
            else:
                first, second = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(second + first)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(second * first)
                elif token == "/":
                    stack.append(int(second / first))
                else:
                    raise ValueError(f"noop: {token}")

        return stack[0]

    def is_num(self, val: str) -> bool:
        try:
            int(val)
            return True
        except:
            return False