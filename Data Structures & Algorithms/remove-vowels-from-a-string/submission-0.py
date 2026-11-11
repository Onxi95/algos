class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        result = []
        for letter in s:
            if letter not in vowels:
                result.append(letter)
        return "".join(result)
