class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_longest = 0
        current_longest = 1

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            current = nums[i]
            if current - prev == 1:
                current_longest += 1
            elif current - prev == 0:
                continue
            else:
                if current_longest > max_longest:
                    max_longest = current_longest

                current_longest = 1

        return current_longest if current_longest > max_longest else max_longest
