class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.lstrip('-').isnumeric():
                stack.append(int(op))
            elif op == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first)
                stack.append(second)
                stack.append(first + second)
            elif op == "C":
                latest = stack.pop()
            else:
                latest = stack.pop()
                stack.append(latest)
                stack.append(latest * 2)

        return sum(stack)