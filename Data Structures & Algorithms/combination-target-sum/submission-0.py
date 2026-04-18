class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index):
            if index >= len(nums):
                if sum(current) == target:
                    result.append(current.copy())
                return
            if sum(current) > target:
                return

            current.append(nums[index])
            backtrack(index)
            current.pop()
            backtrack(index + 1)

        backtrack(0)

        return result