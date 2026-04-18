class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1] * len(arr)
        current_largest = -1

        for i in range(len(arr) -1, 0, -1):
            num = arr[i]
            current_largest = max(current_largest, num)
            result[i - 1] = current_largest

        return result