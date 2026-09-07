class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index: int):
            if index > len(nums) - 1:
                return 0

            if index in memo:
                return memo[index]

            jump_one = dfs(index + 1)
            jump_two = nums[index] + dfs(index + 2)
            max_result = max(jump_one, jump_two)

            memo[index] = max_result

            return max_result

        return dfs(0)