class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(map(lambda x: f"{len(x)}#{x}", strs))
    def decode(self, s: str) -> List[str]:
        result = []
        index = 0

        while index < len(s):
            num = ""
            while s[index] != "#":
                num += s[index]
                index += 1

            num = int(num)
            result.append(s[index + 1: index + 1 + num])
            index += num + 1

        return result