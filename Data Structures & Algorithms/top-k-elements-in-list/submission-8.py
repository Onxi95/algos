from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        pq = []
        for num in count.keys():
            heapq.heappush(pq, (count[num], num))
            if len(pq) > k:
                heapq.heappop(pq)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(pq)[1])

        return result