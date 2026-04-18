class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                if len(stack) < 2:
                    return -1

                second = stack.pop()
                first = stack.pop()

                match token:
                    case "+":
                        stack.append(first + second)
                    case "-":
                        stack.append(first - second)
                    case "*":
                        stack.append(first * second)
                    case "/":
                        stack.append(int(first / second))

            else:
                stack.append(int(token))

        return stack[0]