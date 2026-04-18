from string import ascii_lowercase

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        groups: defaultdict[str, list[str]] = defaultdict(list)

        for string in strings:
            key = ""
            for i in range(1, len(string)):
                prev_idx = ascii_lowercase.index(string[i - 1])
                current_idx = ascii_lowercase.index(string[i])
                diff = (current_idx - prev_idx) % 26

                key += f"{diff},"

            groups[key].append(string)

        return list(groups.values())
