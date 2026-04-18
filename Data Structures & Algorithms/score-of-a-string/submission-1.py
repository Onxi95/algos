class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(0, len(s) - 1):
            current = ord(s[i])
            next = ord(s[i + 1])

            total += abs(next - current)

        return total
