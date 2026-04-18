class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for count in ransom_counter:
            if magazine_counter[count] < ransom_counter[count]:
                return False

        return True