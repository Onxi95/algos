from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(map(lambda p: f"{p[0] if p[0] is not None else ""}{p[1] if p[1] is not None else ""}", zip_longest(word1, word2)))