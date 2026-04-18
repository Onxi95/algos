class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            square_l = nums[left] ** 2
            square_r = nums[right] ** 2

            if square_l > square_r:
                result.insert(0, square_l)
                left += 1
            else:
                result.insert(0, square_r)
                right -= 1
        
        return result