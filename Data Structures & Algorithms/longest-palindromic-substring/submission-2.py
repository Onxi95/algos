class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s: str):
            return s == s[::-1]
        
        result = ""
        for index, letter in enumerate(s):
            left = right = index
            while left >= 0 and right <= len(s) - 1 and is_palindrome(s[left:right + 1]):
                inner = s[left:right + 1]
                result = inner if len(inner) > len(result) else result
                left -= 1
                right += 1

            left = index
            right = index + 1

            while left >= 0 and right <= len(s) - 1 and is_palindrome(s[left:right + 1]):
                inner = s[left:right + 1]
                result = inner if len(inner) > len(result) else result
                left -= 1
                right += 1

        return result