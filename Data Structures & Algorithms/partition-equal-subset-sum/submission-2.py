class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        half_sum = total_sum / 2

        memo = {}

        def dfs(index: int, reminder: int):
            if reminder == 0:
                return True
            if index >= len(nums) or reminder < 0:
                return False

            key = f"{index}-{reminder}"
            if key in memo:
                return memo[key]

            left = dfs(index + 1, reminder - nums[index])
            right = dfs(index + 1, reminder)

            result = left or right
            memo[key] = result

            return result

        return dfs(0, half_sum)
            