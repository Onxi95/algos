from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        scoreboard = Counter(nums)

        return list(map(lambda x: x[0], scoreboard.most_common(k)))