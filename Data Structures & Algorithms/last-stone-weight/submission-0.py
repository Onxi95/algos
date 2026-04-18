class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = sorted(stones, reverse=True)
        while len(result) > 1:
            first = result.pop(0)
            second = result.pop(0)
            result.append(abs(first - second))
            result = sorted(result, reverse=True)
            
        return result[0]
        