class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums, target)
        if nums[pivot] == target:
            return pivot
        if nums[-1] < target:
            return self.binary_search(nums, target, 0, pivot)
        return self.binary_search(nums, target, pivot, len(nums))

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        
    def find_pivot(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        return left