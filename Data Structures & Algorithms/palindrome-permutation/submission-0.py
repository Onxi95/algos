from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        occurences = Counter(s)

        seen_odd = False

        for letter, total in occurences.items():
            if total % 2 == 0:
                continue
            if seen_odd:
                return False
            seen_odd = True

        if len(s) % 2 == 0:
            return True if not seen_odd else False
        return True