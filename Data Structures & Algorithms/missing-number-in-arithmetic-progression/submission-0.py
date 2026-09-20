class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        total_elements = len(arr) + 1
        expected_sum = (arr[0] + arr[-1]) * total_elements // 2
        return expected_sum - sum(arr)