class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in memory:
                return [memory[diff],idx]
            else:
                memory[num] = idx

        return [-1, -1]