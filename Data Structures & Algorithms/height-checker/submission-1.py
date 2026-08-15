class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        total = 0
        for i in range(len(heights)):
            num1 = s[i]
            num2 = heights[i]
            if num1 != num2:
                total += 1

        return total