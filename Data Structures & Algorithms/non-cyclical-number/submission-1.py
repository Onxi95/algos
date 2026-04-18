class Solution:
    def sum_digits(self, n: int) -> int:
        total = 0
        for digit in str(n):
            total += int(digit) ** 2

        return total

    def isHappy(self, n: int) -> bool:
        seen = {n}

        result = n
        while result != 1:
            result = self.sum_digits(result)
            if result in seen:
                return False
            seen.add(result)

        return True