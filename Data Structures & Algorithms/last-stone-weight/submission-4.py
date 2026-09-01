import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if len(stones) else 0

        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            diff = abs(stone_1 - stone_2)
            if diff != 0:
                heapq.heappush(stones, -diff)
            
        return -stones[0] if len(stones) else 0