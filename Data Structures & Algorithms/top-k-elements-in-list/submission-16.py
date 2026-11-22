from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        groups = [[] for _ in range(len(nums))]
        for num in nums:
            counts[num] += 1

        
        for num, values in counts.items():
            groups[values - 1].append(num)
        result = []

        for i in range(len(groups) - 1, -1, -1):
            for num in groups[i]:
                if len(result) == k:
                    return result
                result.append(num)
            
        return result