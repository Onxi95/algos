class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(map(lambda x: f"{len(x)}#{x}", strs))

    def decode(self, s: str) -> List[str]:
        result = []

        left = 0

        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            num = int(s[left:right])
            result.append(s[right + 1:right + num + 1])
            left = right + num + 1

        return result