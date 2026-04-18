class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        len1 = len(sentence1)
        len2 = len(sentence2)
        if len1 != len2:
            return False

        similar_map = defaultdict(set)

        for word1, word2 in similarPairs:
            similar_map[word1].add(word2)
            similar_map[word2].add(word1)

        for i in range(len1):
            word1 = sentence1[i]
            word2 = sentence2[i]

            if word1 == word2:
                continue

            if word1 not in similar_map or word1 not in similar_map[word2]:
                return False

        return True