class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = sum([i for i in range(len(nums) + 1)])
        current_sum = sum(nums)
        return expected_sum - current_sum