class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            square_l = nums[left] ** 2
            square_r = nums[right] ** 2

            if square_l > square_r:
                result.append(square_l)
                left += 1
            else:
                result.append(square_r)
                right -= 1
        
        return result[::-1]