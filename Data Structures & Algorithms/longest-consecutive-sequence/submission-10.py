class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        longest = 0

        for num in unique:
            inner = 1
            n = num
            while (n - 1) in unique:
                inner += 1
                n -= 1

            longest = max(inner, longest)

        return longest