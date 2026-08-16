from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        counts = Counter(words[0])

        for word in words[1:]:
            inner_counts = Counter(word)
            for char in counts:
                counts[char] = min(counts[char], inner_counts[char])

        result = []
        for char, cnt in counts.items():
            result.extend([char] * cnt)

        return result