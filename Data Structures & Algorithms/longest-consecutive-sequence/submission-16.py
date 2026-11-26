class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fast = set(nums)
        largest = 0
        for num in nums:
            if num + 1 in fast:
                continue
            current = 0
            while num in fast:
                current += 1
                num -= 1
            largest = max(largest, current)
        return largest