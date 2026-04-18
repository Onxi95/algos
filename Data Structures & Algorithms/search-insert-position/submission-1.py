class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            guess = nums[middle]
            if guess == target:
                return middle
            elif guess < target:
                left = middle + 1
            else:
                right = middle - 1

        return left