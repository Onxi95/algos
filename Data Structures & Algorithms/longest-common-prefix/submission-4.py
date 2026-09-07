class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        prefix = ""
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return prefix
            prefix += s[i]

        return prefix