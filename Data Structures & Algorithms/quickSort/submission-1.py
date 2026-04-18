# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)

        return pairs
    
    def quickSortHelper(self, arr: List[Pair], start: int, end: int) -> None:
        if start >= end:
            return

        pivot = arr[end]
        left = start

        for i in range(start, end):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        arr[left], arr[end] = arr[end], arr[left]

        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)