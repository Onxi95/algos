class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def backtrack(index: int, nums: List[int]):
            if index >= len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[index])

            backtrack(index + 1, nums)
            subset.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, nums)

        backtrack(0, nums)

        return result