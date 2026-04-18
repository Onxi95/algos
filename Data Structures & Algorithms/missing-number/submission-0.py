class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = sum([i for i in range(len(nums) + 1)])
        return expected_sum - sum(nums)