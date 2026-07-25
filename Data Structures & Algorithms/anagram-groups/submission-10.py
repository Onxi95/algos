from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            counters[key].append(s)

        return list(counters.values())