class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_ptr = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[swap_ptr], nums[i] = nums[i], nums[swap_ptr]
                swap_ptr += 1
