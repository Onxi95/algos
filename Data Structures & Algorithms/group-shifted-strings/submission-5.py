class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strings:
            if len(string) <= 1:
                result[(-999)].append(string)
            else:
                current_distance = []
                for i in range(0, len(string) - 1):
                    letter_1 = string[i]
                    letter_2 = string[i + 1]
                    diff = (ord(letter_2) - ord(letter_1)) % 26
                    current_distance.append(diff)
                result[tuple(current_distance)].append(string)
        return list(result.values())