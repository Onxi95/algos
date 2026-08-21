from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counts = Counter(s1)

        for i in range(len(s2)):
            c = s2[i]
            if c in counts:
                copy = Counter(counts)
                for j in range(i, max(len(s2), len(s1))):
                    char = s2[j]
                    if copy[char] == 0:
                        break
                    copy[char] -= 1
                
                if copy.total() == 0:
                    return True

        return False
