class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            inner = []
            for subset in result:
                inner.append(subset + [num])

            result += inner

        return result