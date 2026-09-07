class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        for index in range(len(nums)):
            if counts[0]:
                nums[index] = 0
                counts[0] -= 1
            elif counts[1]:
                nums[index] = 1
                counts[1] -= 1
            else:
                nums[index] = 2