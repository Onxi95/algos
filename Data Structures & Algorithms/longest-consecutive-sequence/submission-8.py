class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        result = 0
        for num in nums:
            current = num - 1
            local_max = 1
            while current in unique:
                local_max += 1
                current -= 1
            result = max(result, local_max)

        return result