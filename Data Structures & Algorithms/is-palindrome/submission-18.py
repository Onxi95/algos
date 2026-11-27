class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            l_char = s[left].lower()
            r_char = s[right].lower()

            if not l_char.isalnum():
                left += 1
                continue
            if not r_char.isalnum():
                right -= 1
                continue
            
            if left > right:
                return False
            
            if l_char != r_char:
                return False

            left += 1
            right -= 1

        return True
