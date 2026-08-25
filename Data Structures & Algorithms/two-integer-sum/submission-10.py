class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in memory:
                return [memory[diff], index]
            memory[num] = index

        return [-1, -1] 