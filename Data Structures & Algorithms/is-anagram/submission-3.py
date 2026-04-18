from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sAssoc: dict[str, int] = {}
        tAssoc: dict[str, int] = {}

        for letter in s:
            sAssoc[letter] = sAssoc.get(letter, 0) + 1
        for letter in t:
            tAssoc[letter] = tAssoc.get(letter, 0) + 1

        return sAssoc == tAssoc
