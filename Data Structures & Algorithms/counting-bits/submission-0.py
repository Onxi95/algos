class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            total = 0
            while i:
                total += i & 1
                i = i >> 1
            result.append(total)

        return result