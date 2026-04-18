class Solution:
    def scoreOfString(self, s: str) -> int:
        
        total = 0
        for i in range(len(s) - 1):
            curr = ord(s[i])
            adj = ord(s[i + 1])
            total += abs(adj - curr)

        return total