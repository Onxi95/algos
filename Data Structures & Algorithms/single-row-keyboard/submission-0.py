class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        current_index = 0
        current_total = 0
        keyboard_map = {letter: index for index, letter in enumerate(keyboard)}

        for letter in word:
            next_letter_index = keyboard_map[letter]
            diff = abs(current_index - next_letter_index)
            current_total += diff
            current_index = next_letter_index

        return current_total