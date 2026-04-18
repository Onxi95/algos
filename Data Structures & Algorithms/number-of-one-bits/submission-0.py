class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for i in range(32):
            if (1 << i) & n > 0:
                total += 1
        return total