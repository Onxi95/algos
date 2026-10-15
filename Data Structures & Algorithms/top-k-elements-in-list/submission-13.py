from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        for num, count in count.items():
            heapq.heappush(result, (count, num))

            if len(result) > k:
                heapq.heappop(result)

        return list(map(lambda x: x[1], result))