class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        expected = set(range(1, len(nums)))

        for num in nums:
            if num in expected:
                expected.remove(num)
            else:
                return num

        return -1