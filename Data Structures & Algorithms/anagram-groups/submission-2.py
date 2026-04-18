from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for char in s:
                index = ord('z') - ord(char)
                chars[index] += 1
            hashed_key = tuple(chars)

            items[hashed_key].append(s)

        return list(items.values())