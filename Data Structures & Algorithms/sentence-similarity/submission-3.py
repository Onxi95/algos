class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar = set((x, y) for x, y in similarPairs)

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            if (word1, word2) in similar or (word2, word1) in similar:
                continue
            return False

        return True