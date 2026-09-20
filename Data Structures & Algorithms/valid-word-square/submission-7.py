class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for index, word in enumerate(words):
            letters = []
            for j in range(len(word)):
                if j >= len(words):
                    return False
                if index >= len(words[j]):
                    return False
                letter = words[j][index]
                letters.append(letter)
            if "".join(letters) != word:
                return False


        return True