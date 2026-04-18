class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            diff = 0
            while stack and stack[-1][0] < temperature:
                t, i = stack.pop()
                result[i] = index - i
            stack.append((temperature, index))

        return result