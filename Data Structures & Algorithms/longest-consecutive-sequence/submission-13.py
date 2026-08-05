class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        longest = 0
        for num in nums:
            inner_num = num
            inner_longest = 0
            if (num - 1) not in unique: # real start
                while inner_num in unique:
                    inner_num += 1
                    inner_longest += 1
            
            longest = max(longest, inner_longest)

        return longest