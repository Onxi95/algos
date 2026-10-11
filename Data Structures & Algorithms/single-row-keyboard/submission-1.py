class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexes = {letter: index for index, letter in enumerate(keyboard)}
        result = 0
        ptr = 0
        for letter in word:
            distance = abs(indexes[letter] - ptr)
            result += distance
            ptr = indexes[letter]
        return result