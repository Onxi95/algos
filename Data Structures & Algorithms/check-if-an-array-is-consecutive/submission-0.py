class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        largest = max(nums)
        length = len(nums)
        unique = set([(largest - i) for i in range(length)])

        for num in nums:
            if num not in unique:
                return False
            unique.remove(num)

        return True