class Solution:
    def countElements(self, arr: List[int]) -> int:
        items = set(arr)
        total = 0
        for num in arr:
            if num + 1 in items:
                total += 1

        return total