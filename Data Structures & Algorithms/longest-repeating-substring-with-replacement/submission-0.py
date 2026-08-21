from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memory = Counter()
        left = 0
        max_length = 0

        for right in range(len(s)):
            memory[s[right]] += 1
            others = memory.total() - (memory.most_common(1)[0][1])
            if others > k:
                memory[s[left]] -= 1
                left += 1
            else:
                max_length = max(max_length, right - left + 1)

                

        return max_length
