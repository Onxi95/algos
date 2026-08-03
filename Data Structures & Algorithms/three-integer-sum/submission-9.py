class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1

            if num > 0:
                break

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            while left < right:

                num_left = nums[left]
                num_right = nums[right]
                total = num_left + num + num_right

                if total == 0:
                    result.append([num_left, num, num_right])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return result