class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_offset = 0

        if not shift:
            return s

        for direction, increment in shift:
            increment %= len(s)

            if direction == 0:
                s = s[increment:] + s[:increment]
            else:
                s = s[-increment:] + s[:-increment]

        return s