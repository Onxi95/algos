class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index: int, current: List[int], total: int):
            if index >= len(nums) or total > target:
                return
            if total == target:
                result.append(current[:])
                return

            dfs(index, current + [nums[index]], total + nums[index])
            dfs(index + 1, current, total)

        dfs(0, [], 0)

        return result