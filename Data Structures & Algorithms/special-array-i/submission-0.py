class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        
        for i in range(0, len(nums) - 1):
            current = nums[i]
            next = nums[i + 1]
            if current % 2 == next % 2:
                return False

        return True
