class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:

                curr_nums = [nums[left], num, nums[right]]
                if sum(curr_nums) == 0:
                    result.append(curr_nums)
                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                elif sum(curr_nums) < 0:
                    left += 1
                else:
                    right -= 1

        return result
