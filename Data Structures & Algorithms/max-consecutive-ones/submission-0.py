class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest_streak = 0
        ptr = 0

        while ptr < len(nums):
            inner_streak = 0
            while ptr < len(nums) and nums[ptr] == 1:
                inner_streak += 1
                ptr += 1

            largest_streak = max(largest_streak, inner_streak)

            ptr += 1

        return largest_streak