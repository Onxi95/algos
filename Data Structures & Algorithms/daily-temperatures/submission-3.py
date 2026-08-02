class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                prev_i, prev_temperature = stack.pop()
                result[prev_i] = i - prev_i

            stack.append((i, temperature))

        return result