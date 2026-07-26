class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for index, num in enumerate(nums):
            if num > 0:
                break

            if index > 0 and nums[index - 1] == nums[index]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                num_l = nums[left]
                num_r = nums[right]

                total = num + num_l + num_r
                if total == 0:
                    result.append([num, num_l, num_r])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result