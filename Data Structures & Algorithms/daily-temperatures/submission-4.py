class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for index, temperature in enumerate(temperatures[1:]):
            while stack and stack[-1][0] < temperature:
                prev_temperature, prev_idx = stack.pop()
                result[prev_idx] = index + 1 - prev_idx
            stack.append((temperature, index + 1))

        return result        