class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0

        for num in unique:
            current_longest = 1
            inner = num - 1
            while inner in unique:
                current_longest += 1
                inner -= 1
            longest = max(longest, current_longest)

        return longest