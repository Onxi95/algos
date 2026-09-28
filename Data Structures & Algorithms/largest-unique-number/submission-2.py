from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        curr_max = -1
        
        for num, count in count.items():
            if count == 1:
                curr_max = max(curr_max, num)

        return curr_max