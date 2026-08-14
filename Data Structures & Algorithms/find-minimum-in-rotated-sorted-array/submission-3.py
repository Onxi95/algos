class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                minimum = min(nums[left], minimum)
                break
            
            minimum = min(nums[mid], minimum)

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return minimum