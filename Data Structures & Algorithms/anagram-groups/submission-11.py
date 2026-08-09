from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for char in s:
                key[(ord(char) - 97)] += 1

            result[tuple(key)].append(s)

        return list(result.values())