class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_in_window = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in unique_in_window:
                unique_in_window.remove(s[left])
                left += 1
            else:
                max_len = max(max_len, right - left + 1)
            unique_in_window.add(s[right])

        return max_len