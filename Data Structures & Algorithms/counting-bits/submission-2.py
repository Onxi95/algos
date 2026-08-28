class Solution:
    def countBits(self, n: int) -> List[int]:
        return list(map(lambda x: bin(x)[1:].count("1"), range(0, n + 1)))