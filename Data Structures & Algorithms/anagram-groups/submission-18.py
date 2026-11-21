from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)

        for s in strs:
            bucket = [0 for _ in range(26)]
            for char in s:
                index = ord(char) - ord('a')
                bucket[index] += 1
            memo[tuple(bucket)].append(s)

        return list(memo.values())