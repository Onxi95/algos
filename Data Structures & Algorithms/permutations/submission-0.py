class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index: int, toSkip: Set[int], current: List[int]):
            if index >= len(nums):
                result.append(current[:])
                return

            for i, num in enumerate(nums):
                if i in toSkip:
                    continue
                toSkip.add(i)
                backtrack(index + 1, toSkip, current + [nums[i]])
                toSkip.remove(i)

        backtrack(0, set(), [])

        return result