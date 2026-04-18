class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest = 0
        ptr = 0

        while ptr < len(nums):
            inner = 0
            while ptr < len(nums) and nums[ptr] == 1:
                inner += 1
                ptr += 1

            largest = max(largest, inner)
            ptr += 1

        return largest