class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = str(x)

        left = 0
        right = len(n) - 1

        while left < right:
            digit1 = n[left]
            digit2 = n[right]

            if digit1 != digit2:
                return False

            left += 1
            right -= 1

        return True