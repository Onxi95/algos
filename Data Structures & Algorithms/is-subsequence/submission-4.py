class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        substr_ptr = 0

        for letter in t:

            if substr_ptr == len(s):
                return True

            if letter == s[substr_ptr]:
                substr_ptr += 1

        return substr_ptr == len(s)
