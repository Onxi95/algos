class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        longer = word1 if len(word1) >= len(word2) else word2
        shorter = word1 if len(word1) < len(word2) else word2

        index = 0

        while index < len(shorter):
            letter_s = word1[index]
            letter_l = word2[index]

            result.append(letter_s)
            result.append(letter_l)
            index += 1

        return "".join(result) + longer[index:]