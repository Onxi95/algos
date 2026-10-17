class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0 
        unique = set(nums)

        for num in nums:
            current_max = 1
            current_num = num
            if (current_num + 1) not in unique:
                while (current_num - 1) in unique:
                    current_num -= 1
                    current_max += 1

            result = max(result, current_max)

        return result