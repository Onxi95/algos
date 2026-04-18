class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr_idx = len(s) - 1

        while ptr_idx >= 0:
            current = s[ptr_idx]
            if current == " ":
                ptr_idx -= 1
            else:
                break

        last_word_length = 0
        while ptr_idx >= 0 and s[ptr_idx] != " ":
            ptr_idx -= 1
            last_word_length += 1

        return last_word_length
