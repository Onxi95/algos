class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        result = [-1] * size

        current_largest = float("-Inf")

        for i in range(size - 1, 0, -1):
            current = arr[i]
            result_idx = i - 1

            if current > current_largest:
                current_largest = current

            result[result_idx] = int(current_largest)

        return result
