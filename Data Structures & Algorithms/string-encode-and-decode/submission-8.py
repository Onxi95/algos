class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(map(lambda x: f"{len(x)}#{x}", strs))
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            current_len = ""
            j = i
            while s[j] != "#":
                current_len += s[j]
                j += 1
            j += 1
            word_end = j + int(current_len)
            result.append(s[j:word_end])
            i = word_end
        return result