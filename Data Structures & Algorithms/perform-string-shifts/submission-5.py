class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0

        for direction, amount in shift:
            total_shift += -amount if direction == 1 else amount

        total_shift %= len(s)

        return f"{s[total_shift:]}{s[:total_shift]}"