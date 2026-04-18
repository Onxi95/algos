class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.helper(nums, target, mid + 1, right)
        else:
            return self.helper(nums, target, left, mid - 1)