class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in memo:
                return [memo[diff], index]
            memo[num] = index

        return [-1, -1]