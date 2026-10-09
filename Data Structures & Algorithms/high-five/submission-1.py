import heapq 
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = defaultdict(list)

        for idx, score in items:
            scores = students[idx]
            heapq.heappush(scores, score)
            if len(scores) > 5:
                heapq.heappop(scores)
        
        results = []
        for idx in sorted(students.keys()):
            results.append([idx, int(sum(students[idx]) / 5)])
        return results
