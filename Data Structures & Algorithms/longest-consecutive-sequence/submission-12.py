class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        longest = 0

        for num in unique:
            if (num - 1) not in unique:
                counter = 1
                while (num + counter) in unique:
                    counter += 1

                longest = max(counter, longest)

        return longest