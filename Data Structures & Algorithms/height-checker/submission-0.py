class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        diff = 0
        for index, height in enumerate(heights):
            if height != expected[index]:
                diff += 1

        return diff