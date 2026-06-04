from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            bucket = [0] * 26
            for character in s:
                bucket[ord(character) - ord('a')] += 1 
            results[tuple(bucket)].append(s)

        return list(results.values())