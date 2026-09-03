class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        def isdigit(val: str) -> bool:
            try:
                int(val)
                return True
            except ValueError:
                return False

        for operation in operations:
            if isdigit(operation):
                stack.append(int(operation))
            else:
                if operation == "+":
                    stack.append(stack[-1] + stack[-2])
                elif operation == "C":
                    stack.pop()
                elif operation == "D":
                    stack.append(stack[-1] * 2)

        return sum(stack)
