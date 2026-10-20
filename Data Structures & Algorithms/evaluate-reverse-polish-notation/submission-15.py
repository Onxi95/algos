class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def isnum(token: str):
            try:
                int(token)
                return True
            except:
                return False

        for token in tokens:
            if isnum(token):
                stack.append(int(token))
                continue
            num2, num1 = stack.pop(), stack.pop()
            if token == "*":
                stack.append(num1 * num2)
            elif token == "/":
                stack.append(int(num1 / num2))
            elif token == "+":
                stack.append(num1 + num2)
            else:
                stack.append(num1 - num2)

        return stack[0]