class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, num in enumerate(nums):
            if num > 0:
                break

            if index >= 1 and nums[index - 1] == num:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + num + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[left], num, nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
