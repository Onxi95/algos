from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        seen_single = False
        for num, val in count.items():
            if val % 2 != 0 and seen_single:
                return False
            if val % 2 != 0:
                seen_single = True

        return True