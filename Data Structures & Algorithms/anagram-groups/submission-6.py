from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            results[key].append(s)

        result = []

        for key, value in results.items():
            result.append(value)

        return result