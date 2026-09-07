class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {}
        def dfs(index: int):
            if index == len(s):
                return True

            if index in memory:
                return memory[index]

            for word in wordDict:
                if s[index: index + len(word)] == word:
                    result = dfs(index + len(word))
                    if result:
                        return True
                    memory[index] = result
            return False

        return dfs(0)