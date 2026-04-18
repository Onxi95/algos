from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            counted = Counter(s)
            hashed_key = tuple(sorted(counted.items()))
            print(hashed_key)
            result[hashed_key].append(s)

        return list(result.values())