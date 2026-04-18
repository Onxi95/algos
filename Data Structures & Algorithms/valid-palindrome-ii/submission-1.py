class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.validate(s, 0, len(s) - 1, False)

    def validate(self, s: str, left: int, right: int, skip: bool):
        if left > right:
            return True

        letter_l = s[left]
        letter_r = s[right]
        print(letter_l, letter_r)

        if letter_l != letter_r:
            if skip:
                return False
            return self.validate(s, left + 1, right, True) or self.validate(s, left, right - 1, True)
        
        return self.validate(s, left + 1, right - 1, skip)