class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += f"{len(string)}#{string}"

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0

        while index < len(s):
            inner_idx = index
           
            while s[inner_idx] != '#':
                inner_idx += 1

            length = int(s[index:inner_idx])
            word = s[inner_idx + 1:inner_idx + 1 + length]            

            result.append(word)
            index = inner_idx + 1 + length

        return result