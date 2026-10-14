class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        assoc = defaultdict(list)

        for s in strs:
            string_hash = [0] * 26
            for letter in s:
                string_hash[ord(letter) - 97] += 1

            assoc[tuple(string_hash)].append(s)

        return list(assoc.values())