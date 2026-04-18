class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_maximum = nums[0]
        maximum = nums[0]

        for i in range(0, len(nums) - 1):
            current = nums[i]
            next = nums[i + 1]
            if next - current >= 1:
                current_maximum += next
            else:
                maximum = max(current_maximum, maximum)
                current_maximum = next

        return max(current_maximum, maximum)