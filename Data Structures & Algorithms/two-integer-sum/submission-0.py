class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num in memory:
                return [memory[num], i]
            memory[diff] = i