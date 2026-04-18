class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        guess = len(nums)
        for i in range(len(nums)):
            guess ^= i ^ nums[i]

        return guess