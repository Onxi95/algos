class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        largest = -1
        nums.sort(reverse=True)
        
        index = 0
        n = len(nums)
        while index < n:

            if index  == n -1 or nums[index] != nums[index + 1]:
                return nums[index]

            while index < n -1 and nums[index] == nums[index + 1]:
                index += 1

            index += 1

        return -1