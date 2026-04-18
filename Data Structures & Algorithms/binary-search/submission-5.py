class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        
        while start <= end:
            mid = (start + end) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                return self.binarySearch(nums, target, mid + 1, end)
            else:
                return self.binarySearch(nums, target, start, mid - 1)

        return -1