class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}

        for index, num in enumerate(numbers):
            diff = target - num
            if diff in memo:
                return [memo[diff] + 1, index + 1]
            memo[num] = index

        return [-1, -1]
            