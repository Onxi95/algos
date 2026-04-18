class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        result = defaultdict(int)
        for ai, bi in trust:
            result[ai] -= 1
            result[bi] += 1

        for i in range(1, n + 1):
            if result[i] == n - 1:
                return i

        return -1
