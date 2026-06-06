class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        result = 0
        for num in nums:
            if (num - 1) not in unique:
                local_max = 1
                while (num + local_max) in unique:
                    local_max += 1
                result = max(result, local_max)

        return result