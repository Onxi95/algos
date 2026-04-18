class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        assoc = {}
        for index, letter in enumerate(pattern):
            current = words[index]
            if not letter in assoc and not current in assoc:
                assoc[letter] = current
                assoc[current] = letter
            else:
                if not letter in assoc:
                    return False
                c = assoc[letter]
                if c != current:
                    return False
        print(assoc)
        return True