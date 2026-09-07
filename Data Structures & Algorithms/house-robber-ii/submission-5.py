class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}

        without_first = nums[1:]
        without_last = nums[:-1]

        def dfs(index: int, houses: List[int], key: str):
            if index > len(houses) - 1:
                return 0

            cache_key = f"{index}-{key}"
            if cache_key in memo:
                return memo[cache_key]

            first = dfs(index + 1, houses, key)
            second = dfs(index + 2, houses, key) + houses[index]
            result = max(first, second)
            memo[cache_key] = result

            return result

        return max(dfs(0, without_first, "without-first"), dfs(0, without_last, "without-last"))